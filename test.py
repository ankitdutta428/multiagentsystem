import requests

headers = {
    "Authorization": "Bearer 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",
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
