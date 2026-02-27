from langchain_openai import ChatOpenAI
from pydantic import SecretStr

llm = ChatOpenAI(
    model="qwen3:0.6b",
    base_url="xxxx",
    api_key=SecretStr(""),
    streaming=True,
    temperature=0.5,
)

resp = llm.stream("nihao")

for chunk in resp:
    print(chunk.content, end="")
