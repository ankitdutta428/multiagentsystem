from fastapi import FastAPI
from pydantic import BaseModel
from llm_router.master_router import classify_subject
from llm_router.stackexchange_client import fetch_from_stackexchange
from llm_router.specialists import chemistry_specialist, physics_specialist, biology_specialist

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

SUBJECT_HANDLERS = {
    "chemistry": chemistry_specialist.get_answer,
    "physics": physics_specialist.get_answer,
    "biology": biology_specialist.get_answer,
}

@app.post("/ask")
def ask(req: QuestionRequest):
    subject = classify_subject(req.question)
    context = fetch_from_stackexchange(subject, req.question)
    print("STACKEXCHANGE CONTEXT:\n", context)
    answer = SUBJECT_HANDLERS[subject](req.question, context)
    return {
        "subject": subject,
        "answer": answer
    }

