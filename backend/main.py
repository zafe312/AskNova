from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from serpapi_client import search_google
from scraper import extract_text_from_url

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # use specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is live!"}

@app.get("/search")
def search(query: str = Query(..., description="User search query")):
    results = search_google(query)

    enriched_results = []

    for result in results:
        url = result["link"]
        content = extract_text_from_url(url)
        enriched_results.append({
            "title": result["title"],
            "link": url,
            "snippet": result["snippet"],
            "content": content[:2000]  # truncate to limit size
        })

    return {"results": enriched_results}