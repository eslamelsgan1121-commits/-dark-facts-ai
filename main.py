import os
import google.generativeai as genai

API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def generate_script(idea):
    response = model.generate_content(f"Write a professional, dark, and mysterious YouTube script for the topic: {idea}. Target: International audience.")
    return response.text

if __name__ == "__main__":
    idea = "Mariana Trench Mysteries"
    script = generate_script(idea)
    print("Script Generated Successfully:")
    print(script)
