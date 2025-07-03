from flask import Flask, request, jsonify, render_template
import os
from utils.gpt_handler import call_gpt

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        if not user_message:
            return jsonify({"response": "❌ Mesej kosong. Sila taip sesuatu."})
        gpt_response = call_gpt(user_message)
        return jsonify({"response": gpt_response})
    except Exception as e:
        return jsonify({"response": f"❌ Ralat sistem: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
