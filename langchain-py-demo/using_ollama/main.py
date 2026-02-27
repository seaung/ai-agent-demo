from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

# 实例化大模型
llm = ChatOllama(model="qwen3:0.6b", base_url="http://localhost:11434")

# 实例化human message实例
messages = [
    HumanMessage(content="你是谁?"),
]

# 流式调用大模型
resp = llm.stream(messages)

for item in resp:
    print(item.content, end="")
