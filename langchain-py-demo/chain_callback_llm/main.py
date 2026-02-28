from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:0.6b", base_url="http://localhost:11434")

prompt_template = PromptTemplate.from_template(template="你是一名{name}工程师")

chain = prompt_template | llm

resp = chain.stream(input={"name": "python"})

for chunk in resp:
    print(chunk.content, end="")
