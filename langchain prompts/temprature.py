from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4.1-mini', temperature=0)
# here changing the temprature will change the output 
#every time more the temp more changed result

result = model.invoke("write a 5 line poem on cricket")

print(result.content)
