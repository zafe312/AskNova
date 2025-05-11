# 🔍 AskNova AI — Your AI-Powered Google Search Replacement

AskNova AI is a full-stack AI-powered chatbot that replaces traditional search engines. It fetches the top 10 Google search results for any query using SerpAPI, scrapes and summarizes their content using Llama-3.2-70b, and presents a concise, reliable answer — along with source links — in a clean user interface.

---

## 🚀 Features

- 🌐 **Real-Time Google Search** via [SerpAPI](https://serpapi.com/)
- 🧠 **Smart Summarization** using Groq (Llama)
- 🧾 **Content Extraction** from top web pages using `trafilatura`
- 📋 **Cited Answers** that reference real source links
- ⚡ **FastAPI Backend** with REST endpoint
- 💻 **Streamlit Frontend** with user-friendly UI

---

## 🛠️ Tech Stack

| Layer      | Technology        |
|------------|-------------------|
| Frontend   | Streamlit         |
| Backend    | FastAPI, Python   |
| Search API | SerpAPI           |
| LLM        | Llama-3.2-70b    |
| Scraper    | Trafilatura       |

---

## 📂 Project Structure

```
searchai/
│
├── backend/
│   ├── main.py              # FastAPI app with /search endpoint
│   ├── serpapi_client.py    # Handles SerpAPI search
│   ├── scraper.py           # Extracts content from URLs
│   └── summarizer.py        # Summarizes combined content via OpenAI
│
├── frontend/
|   ├──app.py                # Streamlit UI
├── requirements.txt         # Python dependencies
└── README.md                # You're here!
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/zafe312/AskNova.git
cd AskNova
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` File

Create a `.env` file in the root folder:

```env
# /.env
GROQ_API_KEY=your-groq-key
SERPAPI_KEY=your-serpapi-key
```

### 4. Run the FastAPI Backend

```bash
cd backend
uvicorn main:app --reload
```

FastAPI will run at: [http://localhost:8000](http://localhost:8000)

Test it:
```
http://localhost:8000/search?query=elon+musk
```

### 5. Run the Streamlit Frontend

In the frontend folder:

```bash
streamlit run app.py
```

Go to: [http://localhost:8501](http://localhost:8501)

---

## 🧠 How It Works

1. **User Query** → Streamlit UI sends it to `/search` FastAPI endpoint.
2. **Search** → FastAPI uses SerpAPI to fetch top 10 Google results.
3. **Scraping** → Each link is fetched and cleaned using `trafilatura`.
4. **Summarization** → All cleaned content is merged and passed to Llama model with the original question.
5. **Response** → A coherent answer and list of source links are returned to the user.

---

## 📌 Example

### Input:
> Who is Elon Musk?

### Output:
A concise LLM generated summary of Elon Musk based on 10 recent search results, followed by links like:
- [Forbes - Elon Musk Profile](https://forbes.com/...)
- [BBC News](https://bbc.com/...)

---

## 📜 License

MIT License. Free to use and modify.

---

