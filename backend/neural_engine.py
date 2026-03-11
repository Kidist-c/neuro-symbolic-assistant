from google import genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

# --------------------------------------------------
# Configure Gemini API (New SDK)
# --------------------------------------------------

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


# --------------------------------------------------
# Neural Reasoning Function
# Used when symbolic reasoning is not appropriate
# --------------------------------------------------

def ask_llm(question: str):
    """
    Sends a natural language question to Gemini
    and returns a structured JSON response containing
    an answer and a short explanation.

    Parameters
    ----------
    question : str
        User's natural language query.

    Returns
    -------
    dict
        {
            "answer": str,
            "reasoning": str
        }
    """

    prompt = f"""
You are an intelligent assistant in a Hybrid Neuro-Symbolic AI system.

Your task is to answer the user's question clearly and concisely,
then provide a short explanation describing how you reached that answer.

Guidelines:
- Provide a direct and accurate answer.
- Keep explanations simple and easy to understand.
- Avoid unnecessary verbosity.
- If the question is ambiguous, make a reasonable assumption.

User Question:
{question}

Return your response STRICTLY in this JSON format:

{{
  "answer": "your direct answer",
  "reasoning": "brief explanation of how the answer was derived"
}}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        raw_text = response.text.strip()

        try:
            parsed = json.loads(raw_text)
            return parsed

        except json.JSONDecodeError:
            return {
                "answer": raw_text,
                "reasoning": "The response could not be parsed as JSON, so the raw model output was returned."
            }

    except Exception as e:
        return {
            "answer": "An error occurred while generating the response.",
            "reasoning": f"LLM request failed due to: {str(e)}"
        }