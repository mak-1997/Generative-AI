from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv(".env")
db_url = os.getenv("DATABASE_URL")
print(db_url)

client = MongoClient(db_url)
db = client["all_data"]
collection = db["dishes"]
data = collection.find()

for doc in data :
    print(data)