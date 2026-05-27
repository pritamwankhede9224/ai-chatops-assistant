from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import requests
import os

# Load environment variables
load_dotenv(dotenv_path=".env")

# OpenAI setup
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Slack webhook
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

# FastAPI app
app = FastAPI()

# Request model
class IncidentRequest(BaseModel):
    incident: str

# Endpoint
@app.post("/incident-alert")
def analyze_and_send(request: IncidentRequest):

    prompt = f"""
    You are a Senior Cloud & DevOps Engineer.

    Analyze the following production incident.

    Provide:
    1. Root Cause
    2. Impact
    3. Recommended Fix
    4. Prevention Strategy

    Incident:
    {request.incident}
    """

    # OpenAI response
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert cloud incident analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    ai_analysis = response.choices[0].message.content

    # Send to Slack
    slack_message = {
        "text": f"🚨 *AI Incident Analysis*\n\n{ai_analysis}"
    }

    requests.post(SLACK_WEBHOOK_URL, json=slack_message)

    return {
        "status": "Incident analyzed and sent to Slack",
        "analysis": ai_analysis
    }