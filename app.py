from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(dotenv_path=".env")

# OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# FastAPI app
app = FastAPI()

# Input model
class IncidentRequest(BaseModel):
    incident: str

# API endpoint
@app.post("/analyze-incident")
def analyze_incident(request: IncidentRequest):

    prompt = f"""
    You are a Senior Cloud & DevOps Engineer.

    Analyze the following cloud incident.

    Provide:
    1. Root Cause
    2. Impact
    3. Recommended Fix
    4. Prevention Strategy

    Incident:
    {request.incident}
    """

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

    return {
        "analysis": response.choices[0].message.content
    }