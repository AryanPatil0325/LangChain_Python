# initialize LLM models just by providing their provider name and model name
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(
    model="groq:qwen/qwen3.8-27b",
    max_tokens = 1024
)

response = llm.invoke("Introduce yourself in short")
print(response.content)