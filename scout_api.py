import requests

def search_semantic_scholar(query: str, limit: int = 5) -> list[dict]:
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,year,url,citationCount,venue",
    }
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    return r.json().get("data", [])

if __name__ == "__main__":
    topic = input("Enter a topic to search Semantic Scholar: ").strip()
    results = search_semantic_scholar(topic, limit=5)

    print("\nTop results:\n")
    for i, p in enumerate(results, 1):
        print(f"{i}. {p.get('title')} ({p.get('year')})")
        print(f"   Citations: {p.get('citationCount')} | Venue: {p.get('venue')}")
        print(f"   {p.get('url')}\n")
