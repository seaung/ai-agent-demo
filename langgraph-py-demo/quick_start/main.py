from langchain_ollama import ChatOllama
from langgraph.graph import END, StateGraph
from pydantic import BaseModel

llm = ChatOllama(base_url="http://localhost:11434", model="qwen3:0.6b")


class AgentState(BaseModel):
    message: str


def chatbot(state: AgentState) -> dict:
    message = state.message
    replay = llm.invoke(message)
    return {"message": replay.content}


graph_builder = StateGraph(AgentState)
graph_builder.add_node(chatbot)
graph_builder.set_entry_point("chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()


if __name__ == "__main__":
    replay = graph.invoke({"message": "hello"})
    print(replay)
