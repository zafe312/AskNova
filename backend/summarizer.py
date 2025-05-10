import logging
import os
from dotenv import load_dotenv
from pathlib import Path
from groq import Groq

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def summarize_all(query: str, articles: list[str], max_tokens: int = 512) -> str:
    logging.info(f"Text received.")
    combined_text = "\n\n".join(articles)
    if not combined_text:
        return "No content found to answer the query."
    
    prompt = (
        f"The following are snippets from the top 10 Google search results "
        f"about the query: '{query}'. Based on this content, provide a concise, informative answer:\n\n"
        f"{combined_text[:12000]}"  # truncate to avoid token limits
    )

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
            max_tokens=max_tokens
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Summarization error: {e}")
        return "Error summarizing content."