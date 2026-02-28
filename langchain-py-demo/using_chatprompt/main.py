from tempfile import template

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:0.6b", base_url="http://localhost:11434")

# 创建提示词模板
system_chat_prompt_template = ChatPromptTemplate.from_template(
    template="你是一名{role}专家,在{domain}领域特别强", role="system"
)

user_chat_prompt_template = ChatPromptTemplate.from_template(
    template="用户问题:{question}",
    role="human",
)

# chat_prompt_template = ChatPromptTemplate.from_messages(
#     [
#         ("system", "你是一名{role}专家,在{domain}特别强"),
#         ("human", "用户问题{question}"),
#     ]
# )

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        system_chat_prompt_template,
        user_chat_prompt_template,
    ]
)

# 模板+变量=> 提示词
prompt = chat_prompt_template.format_messages(
    role="python", domain="网络安全", question="如何从零到一构建一个web扫描器?"
)

resp = llm.stream(prompt)

for chunk in resp:
    print(chunk.content, end="")
