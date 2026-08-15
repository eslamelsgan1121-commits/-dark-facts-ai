import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents='Write a short, dark, and mysterious YouTube script about the deep ocean.'
)

print("Hello Eslam, The Red Color is Gone Forever!")
print("Generated Script:")
print(response.text)
