from dotenv import load_dotenv
import os

load_dotenv(r"E:\langchain\.env")

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print("Token loaded:", token is not None)