import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = f"https://data.mongodb-api.com/app/{os.getenv('MONGODB_APP_ID')}/endpoint/data/v1/action/findOne"
headers = {
    "Content-Type": "application/json",
    "api-key": os.getenv("MONGODB_API_KEY"),
}
payload = {
    "dataSource": "Cluster0",
    "database": "test",
    "collection": "users",
    "filter": {"name": "Alice"}
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())