from fastapi import FastAPI
from pipeline.search import RAGSearch

app = FastAPI(root_path="api/v1")

rag_search = RAGSearch()

@app.get("/")
def home():
    return {"message" : "Welcome to the Sarkari Dost API"}


@app.get("/query")
def query_endpoint(q: str):
    response = rag_search.search_and_summarize(q, top_k=20)
    return {"query" : q, "response" : response}