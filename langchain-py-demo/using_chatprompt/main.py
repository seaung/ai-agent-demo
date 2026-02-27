from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:0.6b", base_url="http://localhost:11434")

# 创建提示词模板
prompt_template = ChatPromptTemplate.from_template(template="今天是个{doing}")

# 模板+变量=> 提示词
prompt = prompt_template.format(doing="好日子")

resp = llm.stream(prompt)

for chunk in resp:
    print(chunk.content, end="")
