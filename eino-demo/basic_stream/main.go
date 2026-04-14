package main

import (
	"context"
	"errors"
	"fmt"
	"io"
	"log"
	"strings"

	"github.com/cloudwego/eino-ext/components/model/ollama"
	"github.com/cloudwego/eino/schema"
)

func main() {
	llm, err := ollama.NewChatModel(context.Background(), &ollama.ChatModelConfig{
		BaseURL: "http://localhost:11434",
		Model:   "qwen3:0.6b",
	})
	if err != nil {
		log.Fatal(err)
	}

	messages := []*schema.Message{
		schema.SystemMessage("你是一个非常友好的智能助手"),
		schema.UserMessage("你会做什么?"),
	}

	var fullContent strings.Builder

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
			log.Fatal(err)
		}
		fmt.Print(chunk.Content)
		fullContent.WriteString(chunk.Content)
	}

	fmt.Println(fullContent.String())

}
