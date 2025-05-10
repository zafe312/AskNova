import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def search_google(query: str, num_results: int = 10):
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google",
        "num": num_results
    }
    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()
    
    results = []
    for result in data.get("organic_results", [])[:num_results]:
        results.append({
            "title": result.get("title"),
            "link": result.get("link"),
            "snippet": result.get("snippet")
        })
    return results
