package main

import (
	"context"
	"fmt"
	"log"

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
		schema.SystemMessage("你是一个友好的助手"),
		schema.UserMessage("你好你是谁?"),
	}

	response, err := llm.Generate(context.Background(), messages)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(response.Content)
}
