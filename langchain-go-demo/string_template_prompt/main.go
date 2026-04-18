package main

import (
	"fmt"
	"log"

	"github.com/tmc/langchaingo/prompts"
)

func generateStringTemplatePrompt(contentType, subject string) string {
	// 1. 定义模板字符串
	stringPrompt := prompts.NewPromptTemplate(
		"写一个{{.content}}关于{{.subject}}",
		[]string{"content", "subject"},
	)

	// 定义目标变量
	input := map[string]any{
		"content_type": contentType,
		"subject":      subject,
	}

	// 格式化模板
	simple, err := stringPrompt.Format(input)
	if err != nil {
		log.Fatal(err)
	}

	return simple
}

func standardTemplatePrompt(topic, website string) string {
	templateWithPrompts := prompts.PromptTemplate{
		Template:       "Research {{.topic}} on {{.website}}", // 提示词
		InputVariables: []string{"topic", "website"},          // 提示词变量名称
		TemplateFormat: prompts.TemplateFormatGoTemplate,      // 模板类型
	}

	template, err := templateWithPrompts.Format(map[string]any{
		"topic":   topic,
		"website": website,
	})
	if err != nil {
		return ""
	}
	return template
}

func main() {
	fmt.Print(standardTemplatePrompt("hello", "world"))
	fmt.Print(generateStringTemplatePrompt("hello", "world"))
}
