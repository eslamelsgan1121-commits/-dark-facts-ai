import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def generate_script(idea):
    response = client.models.generate_content(
        model='gemini-1.5-flash',
        contents=f"Write a professional, dark, and mysterious YouTube script for the topic: {idea}. Target: International audience."
    )
    return response.text

if __name__ == "__main__":
    idea = "Mariana Trench Mysteries"
    script = generate_script(idea)
    print("Script Generated Successfully:")
    print(script)
