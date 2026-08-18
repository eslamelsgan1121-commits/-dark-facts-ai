import os
import google.generativeai as genai

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is missing!")

genai.configure(api_key=api_key)

def generate_youtube_script():
    # استخدام الموديل الأثبت لتجنب أخطاء الإصدارات
    model = genai.GenerativeModel("gemini-pro")
    
    prompt = "Write a detailed, engaging, and professional 10-minute YouTube video script about deep sea mysteries for an international audience."
    
    print("=== بداية السكريبت ===")
    response = model.generate_content(prompt)
    print(response.text)
    print("=== نهاية السكريبت ===")

if __name__ == "__main__":
    generate_youtube_script()
