import streamlit as st
import requests

API_URL = "http://localhost:8000/search"  # Change if deployed

st.set_page_config(page_title="AskNova AI", page_icon="🔍")

st.title("🔍 AskNova AI")
st.write("Ask anything — I’ll find and summarize the top 10 results from Google.")

query = st.text_input("Enter your query:", placeholder="e.g. Who is Elon Musk?")

if st.button("Search") and query.strip():
    with st.spinner("Searching and summarizing..."):
        try:
            response = requests.get(API_URL, params={"query": query})
            data = response.json()

            st.subheader("📌 Answer")
            st.write(data["answer"])

            st.subheader("🔗 Sources")
            for source in data["sources"]:
                st.markdown(f"- [{source['title']}]({source['link']})")

        except Exception as e:
            st.error("Failed to fetch results. Please check the backend or your query.")
            st.exception(e)
