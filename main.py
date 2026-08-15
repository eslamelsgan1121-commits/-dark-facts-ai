import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def generate_script(idea):
    prompt = f"Write a professional, dark, and mysterious YouTube script for the topic: {idea}. Target: International audience."
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    return response.text

if __name__ == "__main__":
    idea = "Mariana Trench Mysteries"
    script = generate_script(idea)
    print("Script Generated Successfully:")
    print(script)
