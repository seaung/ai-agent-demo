package main

import (
	"context"
	"errors"
	"fmt"
	"io"
	"log"

	"github.com/cloudwego/eino-ext/components/model/ollama"
	"github.com/cloudwego/eino/components/prompt"
	"github.com/cloudwego/eino/compose"
	"github.com/cloudwego/eino/schema"
)

func main() {
	chatTemplate := prompt.FromMessages(
		schema.FString,
		schema.SystemMessage("你是一个{role}"),
		schema.UserMessage("{question}"),
	)

	llm, err := ollama.NewChatModel(context.Background(), &ollama.ChatModelConfig{
		BaseURL: "http://localhost:11434",
		Model:   "qwen3:0.6b",
	})
	if err != nil {
		log.Fatal(err)
	}

	// 创建一条链, 输入的是一个map[string]any, 输出的是一个schema.Message类型
	chain := compose.NewChain[map[string]any, *schema.Message]()
	chain.AppendChatTemplate(chatTemplate).AppendChatModel(llm)

	// 编译这条链
	runable, err := chain.Compile(context.Background())
	if err != nil {
		log.Fatal(err)
	}

	input := map[string]any{
		"role":     "生活助手",
		"question": "你能给我的生活带来些什么呢？",
	}

	// 执行这条链
	output, err := runable.Stream(context.Background(), input)
	if err != nil {
		log.Fatal(err)
	}
	defer output.Close()

	for {
		stream, err := output.Recv()
		if err != nil {
			if errors.Is(err, io.EOF) {
				break
			}
		}

		fmt.Print(stream.Content)
	}
}
