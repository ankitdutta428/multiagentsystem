from dotenv import load_dotenv
import os

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
STACKEXCHANGE_KEY = os.getenv("STACKEXCHANGE_KEY")
