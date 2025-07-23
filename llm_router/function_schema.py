from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load Phi-3 model (once when imported)
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-3-mini-128k-instruct")
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/phi-3-mini-128k-instruct",
    torch_dtype=torch.bfloat16,  # Use float32 if bfloat16 not supported
    device_map="auto"            # Automatically places model on GPU/CPU
)

def generate_llm_response(context: str, query: str) -> str:
    prompt = f"""You are a helpful science tutor.

Context:
{context}

Question:
{query}

Answer:"""

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            temperature=0.7,
            do_sample=True,
            top_k=50,
            top_p=0.95
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True).split("Answer:")[-1].strip()
