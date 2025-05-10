import requests
def search_ddg(query):
    url = "https://api.duckduckgo.com/"
    params = {"q": query, "format": "json"}
    response = requests.get(url, params=params)
    return response.json()
results = search_ddg("Django platform")
print(results["RelatedTopics"])