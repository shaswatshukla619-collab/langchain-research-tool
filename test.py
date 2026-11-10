
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(r"E:\langchain\.env")

print("Current directory:", os.getcwd())
print("ENV file exists:", env_path.exists())

load_dotenv(dotenv_path=env_path, override=True)

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print("Token loaded:", bool(token))

if token:
    print("Token starts with:", token[:5])
