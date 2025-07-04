from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Create a prompt using PromptTemplate
prompt = PromptTemplate(input_variables=["stock_name"], 
            template = "Can you provide detailed fundamental analysis for the stock {stock_name} backed by numbers")

# Chat Model
chat_model = ChatOpenAI(temperature=0)
# LCEL style of creating a chain 
chain = prompt | chat_model

# Creating a chain using LLMChain class
# llm_chain = LLMChain(llm=chat_model, prompt=prompt)

stock_name = 'TESLA'
result = chain.invoke({"stock_name":stock_name})
# result = llm_chain.run(stock_name=stock_name)
print(result.content) # print the result/llm response