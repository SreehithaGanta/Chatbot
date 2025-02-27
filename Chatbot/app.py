from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

# Set up Flask app
app = Flask(__name__)
CORS(app)

# Load API Key securely
GOOGLE_API_KEY = ___________ Google API key_____________
if not GOOGLE_API_KEY:
    raise ValueError("Missing Google API Key!")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_response():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        chat = model.start_chat(history=[])  # Initialize chat instance
        response_raw = chat.send_message(user_input)
        print("User Input:", user_input)
        print("Raw Response:", response_raw)

        response = response_raw.text
        return jsonify({"response": response})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
