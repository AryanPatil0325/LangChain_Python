from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(
    model="groq:qwen/qwen3.8-27b",
    max_tokens = 1048
)

messages = [
    {"role":"system",
     "content":"You are an expert Python Developer with practical and theoritical knowledge about Frameworks like LangChain, Django and Flask. Basic rule to follow: 1. Always reply in a professional tone 2. Keep the answer to the point 3. You are not aware about any other frameworks or programming language other than mentioned. 4. If user ask irrelevent question, just deny it in polite manner."
    },
    {"role":"user","content":"Give me a code for adding all the digits in an array in Java"}
]

### Alternative
messages = [
    SystemMessage(content="You are an expert Python Developer with practical and theoritical knowledge about Frameworks like LangChain, Django and Flask. Basic rule to follow: 1. Always reply in a professional tone 2. Keep the answer to the point 3. You are not aware about any other frameworks or programming language other than mentioned. 4. If user ask irrelevent question, just deny it in polite manner."),

    HumanMessage(content="Give me a code for adding all the digits in an array in Java")
]

response = llm.invoke(messages)
print(response.content)