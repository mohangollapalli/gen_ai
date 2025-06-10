from dotenv import load_dotenv 
from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
# llm = ChatAnthropic(model="claude-opus-4-20250514")
# llm = ChatOllama(model="llama3.2")

response = llm.invoke("Can you explain what a motion picture is?")
print("llm response: ", response) 