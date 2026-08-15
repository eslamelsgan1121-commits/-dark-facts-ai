import os
import google.generativeai as genai

# Configure the API key using the environment variable from GitHub Secrets
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is missing!")

genai.configure(api_key=api_key)

def generate_youtube_script():
    # Using the latest stable approach for generating content
    generation_config = {
        "temperature": 0.7,
        "max_output_tokens": 8192,
    }
    
    # Selecting the reliable model for script generation
    model = genai.GenerativeModel('gemini-1.5-flash', generation_config=generation_config)
    
    prompt = "Write a detailed, engaging, and professional 10-minute YouTube video script about deep sea mysteries for an international audience. Include catchy hooks and narration sections."
    
    print("=== START OF GENERATED SCRIPT ===")
    response = model.generate_content(prompt)
    print(response.text)
    print("=== END OF GENERATED SCRIPT ===")

if __name__ == "__main__":
    generate_youtube_script()
