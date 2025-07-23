import requests
from utils.config import OPENROUTER_API_KEY

headers = {
    "Authorization": "Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

json_payload = {
    "model": "gryphe/mythomax-l2-13b",
    "messages": [
        {"role": "user", "content": "Classify this question: What is SN1 mechanism?"}
    ]
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=json_payload)
print(response.status_code)
print(response.json())
