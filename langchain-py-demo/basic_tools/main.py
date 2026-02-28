from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain_ollama import ChatOllama


@tool
def add(a: int, b: int) -> int:
    return a + b


llm = ChatOllama(model="qwen3:0.6b", base_url="http://localhost:11434")

llm_with_tools = llm.bind_tools([add])

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个非常有用的智能助手,可以使用工具解决问题"),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)
