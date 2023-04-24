from settings import MONGO_URI, DB_NAME
from pymongo import MongoClient

client = MongoClient(MONGO_URI)
db = client[DB_NAME]