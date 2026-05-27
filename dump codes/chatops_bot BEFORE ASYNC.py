from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
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

@app.get("/")
def home():
    return {"status": "AI ChatOps Assistant Running"}

@app.post("/slack/analyze")
def slack_analyze(text: str = Form(...)):

    return JSONResponse(
        content={
            "response_type": "in_channel",
            "text": f"✅ Incident received for analysis:\n\n{text}"
        }
    )