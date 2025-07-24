import requests
from utils.config import OPENROUTER_API_KEY

def classify_subject(question):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}"}
    payload = {
        "model": "gryphe/mythomax-l2-13b",
        "messages": [
            {"role": "system", "content": "You are a classifier. Only classify **science questions** into: physics, chemistry, or biology. If the question is not related to science, return 'non-science'."},
            {"role": "user", "content": question}
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    try:
        raw_output = data["choices"][0]["message"]["content"].strip().lower()
        # Return the **first subject word found** in the output
        for subject in ["physics", "chemistry", "biology"]:
            if subject in raw_output:
                return subject
        return "unknown"
    except Exception as e:
        print("LLM classification failed:", e)
        return "unknown"
