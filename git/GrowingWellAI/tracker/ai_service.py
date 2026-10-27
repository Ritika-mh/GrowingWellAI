
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY) if API_KEY else None


def generate_daily_summary(record):
    if client is None:
        return "AI summary unavailable: Gemini API key is not configured."

    prompt = f"""
You are a child daily-routine assistant.

Generate a short summary in simple language for parents.

Rules:
- Use a maximum of 5 bullet points.
- Keep the entire response under 100 words.
- Combine related information.
- Give only 1 practical suggestion.
- Do not repeat the input unnecessarily.
- Do not diagnose medical conditions or nutritional deficiencies.
- Do not predict the child's growth.
- Mention when information is missing.

Daily record:
Age: {record.child_age}
Date: {record.record_date}
Food: {record.food}
Protein foods: {record.protein_foods}
Sleep: {record.sleep_hours} hours
Outdoor activity: {record.outdoor_minutes} minutes
Study: {record.study_minutes} minutes
Screen time: {record.screen_minutes} minutes
"""

    # try:
    #     response = client.models.generate_content(
    #         # model="gemini-2.5-flash",
    #         model="models/gemini-flash-latest",
    #         contents=prompt,
    #     )
    #     return response.text or "AI did not return a summary."
    # except Exception as e:
    #     print("Exception",e)
    #     return "AI summary could not be generated. Please try again later."

    import time

# Inside generate_daily_summary(), after creating the prompt:

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            return response.text or "AI did not return a summary."

        except Exception as e:
            print(f"Gemini attempt {attempt + 1} failed:", repr(e))

            if attempt < 2:
                time.sleep(2)

    return "AI summary is temporarily unavailable. Please try again later."
