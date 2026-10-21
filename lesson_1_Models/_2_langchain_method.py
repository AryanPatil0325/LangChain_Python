## Using Langchain but GROQ specific

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="qwen/qwen3.8-27b"
)
response = llm.invoke("Hello!, what is your name?")
print(response.content)