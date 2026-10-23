import json


with open("secrets.json", 'r') as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientid"]
CLIENT_SECRET = secrets["clientsecret"]

