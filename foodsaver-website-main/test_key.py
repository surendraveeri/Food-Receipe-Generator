import os
import requests

key = os.getenv("OPENAI_API_KEY")
if not key:
    raise SystemExit("Set OPENAI_API_KEY before running this script.")

r = requests.get(
    "https://api.openai.com/v1/models",
    headers={"Authorization": f"Bearer {key}"},
    timeout=30,
)
print(r.status_code)
print(r.text[:300])
