from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# -----------------------------
# GEMINI API KEYS (fallback)
# -----------------------------
API_KEYS = [os.getenv("GEMINI_API_KEY_1"),
            os.getenv("GEMINI_API_KEY_2")
]        

print("Loaded keys:", API_KEYS)

# ✅ CORRECT MODEL NAME (from your list_models output)
MODEL_NAME = "models/gemini-flash-latest"


# -----------------------------
# FALLBACK FUNCTION
# -----------------------------
def generate_with_fallback(prompt):
    last_error = None

    for key in API_KEYS:
        if not key:
            continue
        try:
            genai.configure(api_key=key)
            model = genai.GenerativeModel(MODEL_NAME)
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            last_error = str(e)
            print("Key failed, trying next...")

    raise Exception(f"All API keys failed. Last error: {last_error}")

# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_design():
    data = request.json

    area = data.get("area")
    bhk = data.get("bhk")
    floors = data.get("floors")
    style = data.get("style")

    if not area or not bhk:
        return jsonify({"error": "Invalid input"}), 400

    prompt = f"""
Describe a conceptual house floor plan in words.

Details:
- Carpet Area: {area} sq ft
- Bedrooms: {bhk} BHK
- Floors: {floors}
- Style: {style}

Explain:
- Room arrangement
- Flow between rooms
- Design style

This is a conceptual description only.
"""

    try:
        result = generate_with_fallback(prompt)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
