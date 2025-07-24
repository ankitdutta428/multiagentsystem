import requests
from utils.config import STACKEXCHANGE_KEY

# Maps each subject to the correct Stack Exchange site name
SITE_MAP = {
    "physics": "physics",
    "chemistry": "chemistry",
    "biology": "biology",
    "bioinformatics": "bioinformatics"  # optional if you expand later
}

def fetch_from_stackexchange(subject, question):
    site = SITE_MAP.get(subject)
    if not site:
        return "Invalid subject or no associated StackExchange site."

    url = (
        f"https://api.stackexchange.com/2.3/search/advanced"
        f"?order=desc&sort=relevance&q={question}&site={site}"
    )

    if STACKEXCHANGE_KEY:
        url += f"&key={STACKEXCHANGE_KEY}"

    response = requests.get(url)
    data = response.json()

    items = data.get("items", [])
    if not items:
        return "No relevant StackExchange results found."

    return "\n".join(
        f"Q: {item['title']}\nA: {item.get('excerpt', '...')}" for item in items[:3]
    )
