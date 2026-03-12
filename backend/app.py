
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from select_reasoning import decide_reasoning
from neural_engine import ask_llm
from metta_engine import MettaEngine

# --------------------------------------------------
# Initialize FastAPI
# --------------------------------------------------

app = FastAPI(
    title="Neuro-Symbolic AI Assistant",
    description="Hybrid system combining symbolic reasoning (MeTTa) and neural LLM reasoning",
    version="1.0"
)
# --------------------------------------------------
# Initialize symbolic engine (loads KB once)
# --------------------------------------------------
metta_engine = MettaEngine()


# --------------------------------------------------
# Request Model
# --------------------------------------------------
class QuestionRequest(BaseModel):
    question: str

# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------
@app.get("/")
def root():
    return {
        "message": "Neuro-Symbolic Assistant Backend Running"
    }
# --------------------------------------------------
# Ask Endpoint
# --------------------------------------------------

@app.post("/ask")
def ask_question(request: QuestionRequest):

    question = request.question

    try:

        # Step 1 — Decide reasoning type
        decision = decide_reasoning(question)
        reasoning_type = decision.get("reasoning_type", "neural")
        query = decision.get("query", question)
        # Step 2 — Route to correct reasoning engine
        if reasoning_type == "forward":
            result = metta_engine.query(query)

        elif reasoning_type == "backward":
            result = metta_engine.query(query)
        else:
            result = ask_llm(query)
        # Step 3 — Return response
        return {
            "question": question,
            "reasoning_type": reasoning_type,
            "query": query,
            "result": result
        }
    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    