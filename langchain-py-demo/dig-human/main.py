from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:0.6b", base_url="http://localhost:11434")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个很有用的助手"),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        # ('placeholder', '{chat_history}'), 消息占位符
        ("human", "{input}"),
    ]
)

# 存储记忆
store = {}


def get_history_session(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


chain = prompt_template | llm

chain_with_message_history = RunnableWithMessageHistory(
    runnable=chain,  # 原始链
    get_session_history=get_history_session,  # 获取聊天记录的方法
    input_messages_key="input",  # 告诉用户输入的问题存储在哪个变量里
    history_messages_key="chat_history",  # 聊天记录获取的key是哪个变量
)

config_session = {"configurable": {"session_id": "lihua_123"}}

response = chain_with_message_history.invoke(
    input={"input": "您好,我的名字叫李华"}, config=config_session
)

print(response)

response1 = chain_with_message_history.invoke(
    input={"input": "你知道我的名字叫什么吗?"}, config=config_session
)

print(response1)
