from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_pyfile("config.py")

# MongoDB connection ->
client = MongoClient(app.config["DB_URL"])
db = client[app.config["DB_NAME"]]