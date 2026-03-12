# decide_reasoning.py
import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

# --------------------------------------------------
# Configure Google Gemini / GenAI API
# --------------------------------------------------
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable.")

client = genai.Client(api_key=API_KEY)


# --------------------------------------------------
# Reasoning Selection Function
# --------------------------------------------------
def decide_reasoning(question: str) -> dict:
    """
    Determines the appropriate reasoning type for a given question
    in a hybrid neuro-symbolic AI system.

    Parameters
    ----------
    question : str
        The user's natural language query.

    Returns
    -------
    dict
        A dictionary containing:
        {
            "reasoning_type": "forward" | "backward" | "neural",
            "query": str  # Formatted query for symbolic reasoning or original question for neural
        }
    """
    prompt = f"""
You are a reasoning selector for a Hybrid Neuro-Symbolic AI system.

Determine the reasoning type for the user's question.

Reasoning types:
- forward: when the user wants to infer, deduce, or know consequences from given facts.
- backward: when the user asks to explain, justify, or prove something.
- neural: for open-ended, ambiguous, or general questions where symbolic reasoning is not suitable.

User Question:
{question}

Return STRICTLY in this JSON format:
{{
    "reasoning_type": "",
    "query": ""
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
            # Validate keys exist
            if "reasoning_type" not in parsed or "query" not in parsed:
                raise ValueError("Missing keys in parsed response.")
            return parsed

        except (json.JSONDecodeError, ValueError):
            # Fallback if JSON parsing fails
            return {
                "reasoning_type": "neural",
                "query": question
            }

    except Exception as e:
        # Handle API errors or connection issues
        return {
            "reasoning_type": "neural",
            "query": question,
            "error": f"Failed to call GenAI API: {str(e)}"
        }


