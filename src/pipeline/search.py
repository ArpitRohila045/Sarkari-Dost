import os
from dotenv import load_dotenv
from pathlib import Path
from .vectorstore import FaissVectorStore
from langchain_groq import ChatGroq

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

class RAGSearch:
    def __init__(self, persist_dir: str = None, embedding_model: str = "all-MiniLM-L6-v2", llm_model: str = "openai/gpt-oss-120b"):
        # Resolve project-root-relative paths to avoid issues when running from notebooks
        from pathlib import Path
        project_root = Path(__file__).resolve().parents[2]
        persist_dir = Path(persist_dir) if persist_dir else project_root / "faiss_store"
        self.vectorstore = FaissVectorStore(str(persist_dir), embedding_model)
        # Load or build vectorstore
        faiss_path = persist_dir / "faiss.index"
        meta_path = persist_dir / "metadata.pkl"
        if not (faiss_path.exists() and meta_path.exists()):
            # use package-local import to avoid ModuleNotFoundError when src is not in sys.path
            from .data_loader import load_all_documents
            docs = load_all_documents(str(project_root / "data"))
            self.vectorstore.build_from_documents(docs)
        
        self.vectorstore.load()
        groq_api_key = os.getenv("GROQ_API_KEY")
        self.llm = ChatGroq(groq_api_key=groq_api_key, model_name=llm_model)
        print(f"[INFO] Groq LLM initialized: {llm_model}")

    def search_and_summarize(self, query: str, top_k: int = 20) -> str:
        results = self.vectorstore.query(query, top_k=top_k)
        texts = [r["metadata"].page_content for r in results if r["metadata"]]
        context = "\n\n".join(texts)
        if not context:
            return "No relevant documents found."
        prompt = f"""
            Act like a human assistance bot, and provide explaination in simple hindi language like you are explaining to a person who is not very much literate.
            Use the following context and Summarize the all schemes by indian government realated to the query.
            Explain each aspect like. eligiblity criteria, documents required, applicatoin process and the deadline into simpple language. 

            query : '{query}'
            \n\nContext:\n{context}\n\nSummary:
        """
        response = self.llm.invoke([prompt])
        return response.content

# Example usage
if __name__ == "__main__":
    rag_search = RAGSearch()
    query = "Accident Insurance Scheme"
    summary = rag_search.search_and_summarize(query, top_k=5)
    print("Summary:", summary)