import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Write a short, dark, and mysterious YouTube script about the deep ocean.'
)

print("Generated Script:")
print(response.text)
