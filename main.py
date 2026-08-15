import os
import google.generativeai as genai
from googleapiclient.discovery import build
from googleapictent.http import MediaFileUpload

API_KEY = "YOUR_GOOGLE_AI_STUDIO_API_KEY"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_script(idea):
    prompt = f"Write a professional, dark, and mysterious YouTube script for the topic: {idea}. Target: International audience."
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    idea = "Mariana Trench Mysteries"
    script = generate_script(idea)
    print(script)
