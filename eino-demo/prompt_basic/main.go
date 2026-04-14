package main

import (
	"context"
	"errors"
	"fmt"
	"io"
	"log"

	"github.com/cloudwego/eino-ext/components/model/ollama"
	"github.com/cloudwego/eino/components/prompt"
	"github.com/cloudwego/eino/schema"
)

func main() {
	promptTemplate := prompt.FromMessages(
		schema.FString,
		schema.SystemMessage("你是一个{role}助手"),
		schema.UserMessage("{question}"),
	)

	promptVariable := map[string]any{
		"role":     "生活",
		"question": "今天吃什么好呢",
	}

	messages, err := promptTemplate.Format(context.Background(), promptVariable)
	if err != nil {
		log.Fatal(err)
	}

	llm, err := ollama.NewChatModel(context.Background(), &ollama.ChatModelConfig{
		BaseURL: "http://localhost:11434",
		Model:   "qwen3:0.6b",
	})
	if err != nil {
		log.Fatal(err)
	}

	stream, err := llm.Stream(context.Background(), messages)
	if err != nil {
		log.Fatal(err)
	}
	defer stream.Close()

	for {
		chunk, err := stream.Recv()
		if err != nil {
			if errors.Is(err, io.EOF) {
				break
			}
		}
		fmt.Print(chunk.Content)
	}
}
