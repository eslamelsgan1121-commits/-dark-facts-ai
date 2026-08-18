import os
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is missing!")

def generate_youtube_script():
    client = genai.Client(api_key=api_key)
    
    prompt = "Write a detailed, engaging, and professional 10-minute YouTube video script about deep sea mysteries for an international audience."
    
    print("=== بداية السكريبت ===")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    print(response.text)
    print("=== نهاية السكريبت ===")

if __name__ == "__main__":
    generate_youtube_script()
