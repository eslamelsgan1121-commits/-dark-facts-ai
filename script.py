import os
import urllib.request
import json

api_key = os.environ.get("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

headers = {'Content-Type': 'application/json'}
data = {
    "contents": [{
        "parts":[{"text": "Act as a professional YouTube scriptwriter for Daily Dark Facts. Write a mysterious script about Deep Sea Mysteries or Pyramid Secrets in English."}]
    }]
}

req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')

try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        print("Script Generated Successfully:")
        print(result)
except Exception as e:
    print(f"Error: {e}")
