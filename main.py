import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

prompt = """
Act as an expert YouTube automated scriptwriter and channel growth manager for a global audience, specializing in dark mysteries, ocean secrets, ancient Egyptian hidden chambers, space mysteries, and pre-sleep anomalous thoughts. 

Write a complete YouTube video script of 9 to 10 minutes length in English. 
Follow this strict structure:
1. THE HOOK: Start the first 5 seconds with an extreme, shocking hook that forces the viewer to stay.
2. CONTENT: Dive deep into one rotation topic: Ocean Mysteries, Pharaohs & Hidden Chambers, Space Secrets, or Pre-sleep Strange Thoughts.
3. CALL TO ACTION (CTA): Insert a strong "Subscribe, hit the bell icon, and share" prompt immediately after the first 5-second hook, then repeat it right after every major thrilling revelation/climax in the middle, and once more just before the ending.
4. SHORTS EXTRACTION: At the very end of your output, provide 2 separate 30-second Short scripts extracted directly from the best, most shocking hooks of this main script.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print("=== GENERATED SCRIPT FOR DAILY DARK FACTS ===")
print(response.text)
