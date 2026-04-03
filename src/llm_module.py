import json
import requests

OPENAI_MODEL = "gpt-4o-mini"


def summarize_profile_with_llm(payload: dict, api_key: str, model: str = OPENAI_MODEL) -> dict:
    """Send one cleaned profile payload to the OpenAI API and return structured JSON insights."""
    if not api_key:
        raise ValueError("Missing OPENAI_API_KEY. Set it before running the program.")

    system_prompt = (
        "You are an analyst turning multi-source profile data into concise business-style insights. "
        "Use only the supplied data. Do not invent facts. Keep the output structured, short, and practical."
    )

    user_prompt = f"""
Analyze this profile dataset and return valid JSON with exactly these keys:
summary, key_strengths, potential_risks, data_observations.

Rules:
- summary: 2 to 3 sentences
- key_strengths: list of 3 short strings
- potential_risks: list of up to 2 short strings
- data_observations: list of 3 short strings
- use only the provided data
- if some fields are missing, work with what is available

Profile data:
{json.dumps(payload, indent=2, default=str)}
"""

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "response_format": {"type": "json_object"},
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.3,
        },
        timeout=60,
    )

    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"]
    return json.loads(content)
