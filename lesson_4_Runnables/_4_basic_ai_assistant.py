"""
Suppose you're building your AI learning assistant. You want two controls:
1. Choose between Qwen and GPT-OSS.
2. Adjust the temperature at runtime.

"""

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import ConfigurableField
from dotenv import load_dotenv

load_dotenv()

default_llm = init_chat_model(model="groq:qwen/qwen3.8-27b",max_tokens = 500, temperature=0)
alt_llm = init_chat_model(model="groq:openai/gpt-oss-120b",max_tokens = 500, temperature=0)

default_llm = default_llm.configurable_fields(temperature=ConfigurableField(id="temperature"))
alt_llm = alt_llm.configurable_fields(temperature=ConfigurableField(id="temperature"))

config_model = default_llm.configurable_alternatives(
    ConfigurableField(id="model_choice"),
    default_key="default_llm",
    alt_llm = alt_llm
)

prompt = ChatPromptTemplate.from_messages([
    {'role':'system','content':'You are an expert philosopher, who has an capability to write short touchy quotes in 2 lines.'},
    {'role':'user','content':'Write a quote on {topic}'}
])

chain = prompt | config_model 

response = chain.invoke({'topic':'Life'},config={'configurable':{'model_choice':'default_llm','temperature':1}})

print(f"Quote <using {response.response_metadata['model_name']}>\n{response.content}")