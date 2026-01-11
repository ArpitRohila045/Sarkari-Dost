from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from .pipeline.search import RAGSearch 
from typing import Optional

app = FastAPI()
rag_search = RAGSearch()

class QueryRequest(BaseModel):
    query : str = Field(..., min_length=1)
    top_k : int = Field(5, gt=1, lt=50)
    language : str = Field("hindi", min_length=2)

class QueryResponse(BaseModel):
    query : str 
    response : str

@app.get("/api/v1/home")
def home():
    return {"message" : "Welcome to the Sarkari Dost API"}


@app.post("/api/v1/query" , status_code=200, response_model=QueryResponse)
async def query_endpoint(payload : QueryRequest):
    response = rag_search.search_and_summarize(
        payload.query,
        payload.top_k
    )
    if not response:
        raise HTTPException(status_code=500, detail="Failed to get response")
    
    return {"query" : payload.query, "response" : response}