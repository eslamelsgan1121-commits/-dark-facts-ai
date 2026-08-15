import os
import urllib.request
import json

api_key = os.environ.get('GEMINI_API_KEY')

if not api_key:
    print("Error: GEMINI_API_KEY is not set.")
    exit(1)

url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={api_key}"
headers = {'Content-Type': 'application/json'}

data = {
    "contents": [{
        "parts": [{"text": "Write a short, engaging YouTube script for Daily Dark Facts about deep sea mysteries. Output only the script text."}]
    }]
}

req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')

try:
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode('utf-8'))
        script_text = res['candidates'][0]['content']['parts'][0]['text']
        print(script_text)
except Exception as e:
    print(f"Error: {e}")
