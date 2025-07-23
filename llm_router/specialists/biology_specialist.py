import requests
from utils.config import OPENROUTER_API_KEY
from llm_router.stackexchange_client import get_stackexchange_context  

def get_answer(question, context):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}"}
    payload = {
        "model": "microsoft/phi-3-mini-128k-instruct",
        "messages": [
            {"role": "system", "content": "You are a biology expert. Use the context below to answer the user's question accurately."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"}
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]

def answer_query(question):
    context = get_stackexchange_context("biology", question)  
    return get_answer(question, context)
