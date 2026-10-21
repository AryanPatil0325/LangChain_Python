from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(
    model="groq:qwen/qwen3.8-27b"
)

prompt = ChatPromptTemplate.from_messages([
    {"role":"system","content":"You are an expert in {language} development and a coding assistant"},
    {"role":"user","content":"{query}"}
])

input = {"language":"Python","query":"Write a code to print a message"}

formatted_prompt = prompt.format_messages(**input)
print("using .format_messages",formatted_prompt)
print()
alternative = prompt.invoke({"language":"Python","query":"Write a code to print a message"})
print("using .invoke",alternative)

response = llm.invoke(formatted_prompt)
print(response.content)
