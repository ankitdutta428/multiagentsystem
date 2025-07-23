import requests
from utils.config import STACKEXCHANGE_KEY

# Maps each subject to the correct Stack Exchange site
SITE_MAP = {
    "physics": "physics",
    "chemistry": "chemistry",
    "biology": "biology",
    "bioinformatics": "bioinformatics"  # Optional
}

def get_stackexchange_context(subject: str, question: str) -> str:
    site = SITE_MAP.get(subject.lower())
    if not site:
        return f"No Stack Exchange site found for subject '{subject}'."

    url = (
        "https://api.stackexchange.com/2.3/search/advanced"
        f"?order=desc&sort=relevance&q={question}&site={site}&filter=withbody"
    )

    if STACKEXCHANGE_KEY:
        url += f"&key={STACKEXCHANGE_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        return f"Error fetching from Stack Exchange API: {e}"

    items = data.get("items", [])
    if not items:
        return "No relevant Stack Exchange results found."

    context_parts = []
    for item in items[:3]:  # Top 3 results
        title = item.get("title", "No title")
        link = item.get("link", "")
        excerpt = item.get("excerpt", "No excerpt available.")
        context_parts.append(f"Q: {title}\nA: {excerpt}\n🔗 {link}\n")

    return "\n".join(context_parts)
