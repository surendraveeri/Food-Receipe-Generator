import json
import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise SystemExit("Set GEMINI_API_KEY before running this script.")

MODEL = "gemini-2.5-flash"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1/models/{MODEL}:generateContent?key={API_KEY}"

payload = {
    "contents": [
        {
            "role": "user",
            "parts": [{"text": "Say hello world!"}],
        }
    ]
}

print("Sending request to Gemini 2.5 Flash...")
response = requests.post(
    ENDPOINT,
    headers={"Content-Type": "application/json"},
    data=json.dumps(payload),
    timeout=30,
)

print("Status:", response.status_code)
print("Response:")
print(response.text)
