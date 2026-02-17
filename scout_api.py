# This library lets Python talk to websites and APIs
import requests

# This function searches Semantic Scholar for papers
# query = the topic to search for
# limit = how many papers to return (default is 5)
def search_semantic_scholar(query: str, limit: int = 5) -> list[dict]:
    # This is the address of the Semantic Scholar search API
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    
    # These are the search settings we send to the API
    # We specify:
    # - what to search for
    # - how many results we want
    # - which fields of information to return
    
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,year,url,citationCount,venue",
    }

    # Send the request to Semantic Scholar
    # This is like opening a web page, but in code
    r = requests.get(url, params=params, timeout=30)

    # If something went wrong (for example the API is down),
    # this will raise an error instead of failing silently
    r.raise_for_status()

    # Convert the response from JSON into Python data
    # and return the list of papers
    return r.json().get("data", [])

# This part only runs when we run this file directly
if __name__ == "__main__":
    # Ask the user to type a topic
    topic = input("Enter a topic to search Semantic Scholar: ").strip()
    # Call our search function using that topic
    results = search_semantic_scholar(topic, limit=5)

    print("\nTop results:\n")
    # Loop through each paper and print useful details
    for i, p in enumerate(results, 1):
        print(f"{i}. {p.get('title')} ({p.get('year')})")
        print(f"   Citations: {p.get('citationCount')} | Venue: {p.get('venue')}")
        print(f"   {p.get('url')}\n")
