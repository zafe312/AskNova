import trafilatura

def extract_text_from_url(url: str) -> str:
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            result = trafilatura.extract(downloaded, include_comments=False, include_tables=False)
            return result if result else ""
        return ""
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""
