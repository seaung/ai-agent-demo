package main

import (
	"context"
	"fmt"
	"log"
	"strings"

	"github.com/cloudwego/eino/compose"
)

func main() {
	chain := compose.NewChain[string, string]()

	chain.AppendLambda(compose.InvokableLambda(func(ctx context.Context, input string) (string, error) {
		result := strings.ToLower(input)
		return result, nil
	})).AppendLambda(compose.InvokableLambda(func(ctx context.Context, input string) (string, error) {
		result := strings.ToUpper(input)
		return result, nil
	}))

	runnable, err := chain.Compile(context.Background())
	if err != nil {
		log.Fatal(err)
	}

	resp, err := runnable.Invoke(context.Background(), "hello world")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Print(resp)
}
