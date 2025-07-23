import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from llm_router import master_router
from llm_router.specialists import biology_specialist, chemistry_specialist, physics_specialist
from llm_router.function_schema import generate_llm_response

def handle_query(query: str) -> str:
    # Step 1: Classify subject
    subject = master_router.classify_subject(query)
    print(f"[Classifier] Identified subject: {subject}")

    # Step 2: Route to subject specialist
    if subject == "biology":
        context = biology_specialist.answer_query(query)
    elif subject == "chemistry":
        context = chemistry_specialist.answer_query(query)
    elif subject == "physics":
        context = physics_specialist.answer_query(query)
    else:
        return "❌ Could not determine subject."

    # Step 3: Generate LLM-based final response
    final_response = generate_llm_response(context, query)
    return final_response

# 🔽 Run the interactive loop
if __name__ == "__main__":
    print("🔬 Science Query Assistant")
    print("---------------------------")
    while True:
        user_query = input("\n🧠 Ask a science question (or type 'exit'): ")
        if user_query.strip().lower() == "exit":
            break
        answer = handle_query(user_query)
        print(f"\n📘 Final Answer:\n{answer}\n")
