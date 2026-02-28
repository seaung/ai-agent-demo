from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:0.6b", base_url="http://localhost:11434")

prompt_template = PromptTemplate.from_template("你是一名{name}")

prompt = prompt_template.format(name="python工程师")

resp = llm.stream(prompt)

for chunk in resp:
    print(chunk.content, end="")
