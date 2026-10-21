import os # to interact with .env
from dotenv import load_dotenv # load the variables from .env
from groq import Groq # provider

load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")

client = Groq()
# client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model = "qwen/qwen3.8-27b",
    messages=[
        {
            "role":"user",
            "content":"How are you?"
        }
    ],
    max_tokens=1024
)
# printing the entire response
print("Response:\n",response)
print("Model name:",response.model)
print("Role:",response.choices[0].message.role)
print("Content:",response.choices[0].message.content)
print("Usage:\n",response.usage)