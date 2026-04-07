from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:0.6b", base_url="http://localhost:11434", temperature=0.3)

history = [{"role": "system", "content": "你是一个很厉害的学习助手"}]

history.append({"role": "human", "content": "什么是langchain"})

resp = llm.invoke(history)

print("[first]: ")
print(resp.content)

history.append({"role": "human", "content": "langchain的核心组件有哪些？"})

resp = llm.invoke(history)

print("[second]: ")
print(resp.content)

history.append({"role": "human", "content": "给一个使用例子"})

resp = llm.invoke(history)
print("[thir]: ")
print(resp.content)
