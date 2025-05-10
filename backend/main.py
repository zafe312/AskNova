from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from serpapi_client import search_google

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
    return {"results": results}