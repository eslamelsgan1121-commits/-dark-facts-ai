import os
import google.generativeai as genai

# Setup API Key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Use the most robust model for standard generation
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = "Write a 9-minute YouTube script about Space Secrets. Include a hook, three calls to subscribe, and two 30-second Short scripts at the end."

# Generate
response = model.generate_content(prompt)

print("=== SCRIPT GENERATED ===")
print(response.text)
