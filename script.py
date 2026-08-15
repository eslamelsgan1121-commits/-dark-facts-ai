import os
import requests
import json

def generate_script():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY is not set.")
        return

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{
            "parts":[{"text": "Act as a professional YouTube scriptwriter for Daily Dark Facts. Write a mysterious script about Deep Sea Mysteries, Pyramid Secrets, Pharaohs Curse, Space Mysteries, or Midnight Thoughts. Provide the result in English."}]
        }]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        print("Script successfully generated!")
        print(data['candidates'][0]['content']['parts'][0]['text'])
    except Exception as e:
        print(f"System Error: {e}")

if __name__ == "__main__":
    generate_script()
