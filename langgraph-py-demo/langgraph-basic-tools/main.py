from datetime import datetime
from typing import Annotated, List

from langchain.tools import tool
from langchain_ollama.chat_models import ChatOllama
from langgraph.graph import END, StateGraph, add_messages
from langgraph.prebuilt import ToolNode
from pydantic import BaseModel, Field


@tool
def get_weather(loc: str):
    """获取指定地理位置的当前天气
    Args:
        loc: 地理位置，如"广东"、"北京"等
    Return:
        返回天气描述字符串
    """
    now_date = datetime.now()  # 在函数内部获取当前时间，不依赖 LLM 传入
    return f"{now_date.date()} {loc}的天气很好，风和日丽"


llm = ChatOllama(base_url="http://localhost:11434", model="qwen3:0.6b")

tools = [get_weather]
tool_node = ToolNode(tools)

llm_with_tools = llm.bind_tools(tools)


class WeatherState(BaseModel):
    messages: Annotated[List, add_messages] = Field(
        default=[], description="智能体传递的消息"
    )


def chatbot(state: WeatherState):
    response = llm_with_tools.invoke(state.messages)
    return {"messages": [response]}


graph_build = StateGraph(WeatherState)
graph_build.add_node("chatbot", chatbot)
graph_build.add_node("tools", tool_node)
graph_build.set_entry_point("chatbot")
graph_build.add_edge("chatbot", "tools")
graph_build.add_edge("tools", END)

graph = graph_build.compile()


if __name__ == "__main__":
    user_input = "帮我查一下广东的天气"
    init_state = {"messages": user_input}
    result = graph.invoke(init_state)
    print(result["messages"][-1].content)
