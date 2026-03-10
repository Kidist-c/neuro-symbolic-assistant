from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Neuro-Symbolic Assistant Backend")

# Define request model
class QuestionRequest(BaseModel):
    question: str

# Simple test route
@app.get("/")
def home():
    return {"message": "Neuro-Symbolic Assistant Backend Running"}

# Placeholder /ask route
@app.post("/ask")
def ask_question(request: QuestionRequest):
    # For now, just echo the question
    return {
        "question_received": request.question,
        "answer": "This will be replaced by LLM or PETTA later",
        "trace": {
            "router": "not yet implemented",
            "reasoning": "not yet implemented",
            "engine": "not yet implemented"
        }
    }