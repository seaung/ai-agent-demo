package main

import (
	"context"
	"fmt"
	"log"

	"github.com/tmc/langchaingo/llms"
	"github.com/tmc/langchaingo/llms/ollama"
)

func main() {
	llm, err := ollama.New(
		ollama.WithModel("qwen3:0.6b"),
		ollama.WithServerURL("http://localhost:11434"),
	)

	if err != nil {
		log.Fatal(err)
	}

	prompt := "李白是谁?"

	completion, err := llms.GenerateFromSinglePrompt(context.Background(), llm, prompt)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Print(completion)
}
