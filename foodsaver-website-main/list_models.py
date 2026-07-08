import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise SystemExit("Set GEMINI_API_KEY before running this script.")

url = f"https://generativelanguage.googleapis.com/v1/models?key={API_KEY}"

print("Listing available models...")
r = requests.get(url, timeout=30)

print("Status:", r.status_code)
print("Response:")
print(r.text)
