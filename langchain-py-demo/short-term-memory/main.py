from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver

model = ChatOllama(model="qwen3:0.6b", base_url="http://localhost:11434")

agent = create_agent(model=model, checkpointer=InMemorySaver())

resp = agent.invoke(
    {"messages": [{"role": "human", "content": "你好，我的名字叫李华"}]},
    {"configurable": {"thread_id": "1"}},
)

print(resp)

resp = agent.invoke(
    {"messages": [{"role": "human", "content": "我的名字叫什么？"}]},
    {"configurable": {"thread_id": "1"}},
)

print(resp)
