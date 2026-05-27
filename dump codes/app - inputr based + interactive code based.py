from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from dotenv import load_dotenv
import os

load_dotenv()


# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Take incident input from user
incident_data = input("Enter cloud incident details:\n")

# Build prompt
prompt = f"""
You are a Senior Cloud & DevOps Engineer.

Analyze the following cloud infrastructure incident.

Provide:
1. Root Cause
2. Impact
3. Recommended Fix
4. Prevention Strategy

Incident Details:
{incident_data}
"""

# Send request to OpenAI
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

# Print output
print("\n===== AI INCIDENT ANALYSIS =====\n")
print(response.choices[0].message.content)