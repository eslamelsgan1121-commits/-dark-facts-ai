import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

prompt = """
Act as a professional YouTube content creator for a channel called 'Daily Dark Facts'.
Your goal is to write a deep, engaging, and dark mystery script of 9 to 10 minutes in length.
Choose ONE topic from: Ocean Mysteries, Ancient Egyptian Hidden Chambers, Space Secrets, or Pre-sleep Anomalous Thoughts.

Structure your script strictly as follows:
1. THE HOOK (0:00-0:10): Start with an extremely shocking and mysterious fact that grabs attention immediately.
2. CTA 1 (0:10-0:15): Clearly say: "Before we dive deeper into this mystery, make sure to subscribe, hit the bell icon, and share this video with your friends."
3. MAIN CONTENT (0:15-9:00): Write a detailed, thrilling, and informative deep-dive. Use storytelling.
4. CTA 2 (Middle of content): After a major thrilling revelation, insert: "This is getting crazy! If you're enjoying these facts, subscribe and join the family for more dark mysteries."
5. CTA 3 (Near the end): Before the final conclusion, say: "We are almost at the end of this journey. Don't forget to subscribe and turn on notifications so you don't miss our next mystery!"
6. CONCLUSION (9:00-10:00): Summarize and leave a final haunting thought.

At the very end of your response, provide 2 separate 30-second Short scripts (Hooks) designed to make viewers click the long video.
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

print("=== DAILY DARK FACTS SCRIPT GENERATED ===")
print(response.text)
