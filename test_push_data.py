import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("Mongo_Uri")

# Create a new client and connect to the server
#client = MongoClient(uri)
#print(client)


try:
    #client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    client = MongoClient(uri, tls=True, tlsAllowInvalidCertificates=True, serverSelectionTimeoutMS=5000)

    client.server_info()  # forces a real DB call, no ICMP involved
    print("✅ Successfully connected to MongoDB Atlas")
except Exception as e:
    print("❌ Could not connect:", e)
# Send a ping to confirm a successful connection
#try:
#    client.admin.command('ping')
#    print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
#    print(e)