import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
uri = os.getenv("Mongo_Uri")

client = MongoClient(uri, tls=True, tlsAllowInvalidCertificates=True)
db = client.get_database()
print("Connected to:", db.name)