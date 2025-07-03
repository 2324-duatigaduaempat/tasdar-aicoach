import requests
import os

def call_gpt(user_message):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "⚠️ OPENAI_API_KEY not set."

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_message}],
        "temperature": 0.7
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)

    if response.status_code != 200:
        return f"❌ GPT API Error: {response.text}"

    result = response.json()
    return result['choices'][0]['message']['content']
