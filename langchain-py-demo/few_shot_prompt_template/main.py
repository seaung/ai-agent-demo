from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:0.6b", base_url="http://localhost:11434")

example_template = "输入:{input}\n输出:{output}"

examples = [
    {"input": "将'你好'翻译成英文", "output": "hello"},
    {"input": "将'再见'翻译成英文", "output": "goodbye"},
]

few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate.from_template(example_template),
    prefix="请将下面的中文翻译成中文",
    suffix="输入:{text}\n输出:",
    input_variables=["text"],
)

prompt = few_shot_prompt_template.format(text="谢谢你")

resp = llm.stream(prompt)

for chunk in resp:
    print(chunk.content, end="")
