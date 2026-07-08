from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import json
import os
import requests

# Load environment variables
load_dotenv()

# Read API key from Render Environment Variables
API_KEY = os.getenv("GEMINI_API_KEY")

MODEL = "gemini-2.5-flash"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1/models/{MODEL}:generateContent"

app = Flask(__name__)
CORS(app)


# Home Page
@app.route("/")
def home():
    return render_template("foodsaver.html")


@app.route("/foodtracker")
def foodtracker():
    return render_template("foodtracker.html")


@app.route("/recipegenius")
def recipegenius():
    return render_template("recipegenius.html")


@app.route("/myitems")
def myitems():
    return render_template("myitems.html")


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


@app.route("/additems")
def additems():
    return render_template("additems.html")


@app.route("/mainpg")
def mainpg():
    return render_template("mainpg.html")


@app.route("/smartrecipes")
def smartrecipes():
    return render_template("smartrecipes.html")


@app.route("/setremainders")
def setremainders():
    return render_template("setremainders.html")


# Recipe API
@app.route("/generate_recipe", methods=["POST"])
def generate_recipe():
    try:
        if not API_KEY:
            return jsonify({
                "error": "GEMINI_API_KEY environment variable is not set"
            }), 500

        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        ingredients = data.get("ingredients", "").strip()

        if not ingredients:
            return jsonify({"error": "No ingredients provided"}), 400

        prompt = f"""
Create 3 creative recipes using these ingredients:
{ingredients}

For each recipe provide:

1. Recipe Name
2. Ingredients
3. Step-by-step Instructions

Keep the recipes simple and easy to cook.
"""

        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }

        response = requests.post(
            f"{ENDPOINT}?key={API_KEY}",
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=30
        )

        if response.status_code != 200:
            print(response.text)
            return jsonify({"error": response.text}), 500

        result = response.json()

        recipe = (
            result.get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [{}])[0]
            .get("text", "")
        )

        return jsonify({"recipes": recipe})

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )