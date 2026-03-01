from langchain.agents import AgentState, create_agent
from langchain.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_ollama.chat_models import ChatOllama
from pydantic import BaseModel
from pydantic.fields import Field


class AddInputArgs(BaseModel):
    a: int = Field(description="first number")
    b: int = Field(description="second number")


@tool(
    description="add two numbers",
    args_schema=AddInputArgs,
    return_direct=True,
)
def add(a, b):
    """add two numbers"""
    return a + b


def create_calc_tools():
    return [add]


calc_tools = create_calc_tools()

llm = ChatOllama(model="qwen3:0.6b", base_url="http://localhost:11434")

agent = create_agent(
    model=llm, tools=calc_tools, system_prompt="你是一个计算专家擅长使用工具计算"
)


input = {"messages": [{"role": "human", "content": "1+1=?"}]}

resp = agent.stream(input=input)

for chunk in resp:
    print(chunk)
