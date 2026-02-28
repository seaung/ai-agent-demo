from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:0.6b", base_url="http://localhost:11434")

system_chat_message_template = ChatMessagePromptTemplate.from_template(
    template="你是一个名高级的{enginner}工程师", role="system"
)

human_chat_message_template = ChatMessagePromptTemplate.from_template(
    template="用户问题:{question}",
    role="human",
)

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        system_chat_message_template,
        human_chat_message_template,
    ]
)

prompt = chat_prompt_template.format_messages(
    enginner="python工程师",
    question="怎么开发一套可视化的爬虫系统?",
)

resp = llm.stream(prompt)

for chunk in resp:
    print(chunk.content, end="")
