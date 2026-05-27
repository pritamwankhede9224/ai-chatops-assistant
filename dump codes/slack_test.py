import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(dotenv_path=".env")

webhook_url = os.getenv("SLACK_WEBHOOK_URL")

message = {
    "text": "🔥 AI Incident ChatOps Assistant is now connected!"
}

response = requests.post(webhook_url, json=message)

print(response.status_code)
print(response.text)