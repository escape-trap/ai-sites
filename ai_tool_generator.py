import os
import json
import requests

GEMINI_KEY = os.getenv("GEMINI_API_KEY")

PROMPT = """
Create a SINGLE useful online tool for real users.
Rules:
- No fake promises
- No medical or financial advice
- Simple JavaScript logic
- SEO-friendly
- AdSense compliant

Return JSON with:
{
  "name": "Tool Name",
  "description": "One sentence benefit",
  "keywords": ["keyword1", "keyword2"],
  "js_code": "function logic here"
}
"""

try:
    res = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
        params={"key": GEMINI_KEY},
        json={"contents":[{"parts":[{"text": PROMPT}]}]},
        timeout=30
    )
    
    if res.status_code != 200:
        print(f"Error: {res.status_code}")
        exit(1)
    
    data = res.json()
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    tool = json.loads(text)
    
    with open("tool.json", "w") as f:
        json.dump(tool, f, indent=2)
    
    print("✅ Tool generated successfully")

except Exception as e:
    print(f"❌ Generation failed: {e}")
    exit(1)