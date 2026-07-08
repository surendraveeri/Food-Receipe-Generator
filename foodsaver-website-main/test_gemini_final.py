import os
import google.generativeai as genai

api_key = os.getenv("AIzaSyB7hSLfmWxZX353BVGZoi1eahPy4LU7A5Q")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY before running this script.")

genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content("Say hello world!")
    print("Gemini API working!")
    print(response.text)

except Exception as e:
    print("Gemini error:", e)
