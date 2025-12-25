# 🏛️ Sarkari Dost (Government Friend)

Bridging the Last Mile between Government Schemes and Global Citizens.

Sarkari Dost is an AI-powered "Conversational Bridge" designed to eradicate the digital and linguistic divide in India. It transforms complex, English-centric government portals into simple, voice-based experiences in regional dialects, specifically targeting the "next billion" users.

## 🚀 The Vision

Over 250 million rural citizens are eligible for government welfare but fail to apply due to:

- **Information Asymmetry:** Complex legal and bureaucratic language.
- **Linguistic Barriers:** Most portals support only English or formal Hindi.
- **Form Anxiety:** The psychological fear of making errors on official documents.

Sarkari Dost acts as a localized mediator, using voice-first AI to make Digital Public Infrastructure (DPI) accessible to everyone, regardless of their literacy level or language.

## 🛠️ Tech Stack

| Layer      | Technology                | Purpose                                                      |
|------------|--------------------------|--------------------------------------------------------------|
| Frontend   | React (SPA) / PWA        | High performance on low-end devices; offline caching.        |
| Voice/NLP  | Bhashini APIs            | ASR, TTS, and NMT for 22+ Scheduled Indian Languages.        |
| Brain (LLM)| Llama 3.3 (via Groq)     | Ultra-low latency reasoning for real-time conversation.      |
| RAG Pipeline | LangChain + Pinecone   | Ensures hallucination-free retrieval from verified sources.  |
| OCR        | Google Vision / IIIT-H   | Extracting data from physical ID cards.                      |
| Backend    | FastAPI + Supabase       | Scalable, async processing of voice streams.                 |

## 🏗️ Technical Architecture: Agentic RAG

The system follows a sophisticated Retrieval-Augmented Generation (RAG) pattern:

1. **Ingestion:** Python scripts utilizing Firecrawl scrape portals like myScheme.gov.in into clean, structured data.
2. **Indexing:** Data is "chunked" and stored in a Vector Database (Pinecone).
3. **The Request:** User asks a question in a regional dialect (e.g., Marathi or Tamil) via voice.
4. **Translation:** Bhashini converts Voice → Regional Text → English.
5. **Reasoning:** The LLM searches the Vector DB, identifies eligibility, and synthesizes a simple summary.
6. **Response:** The summary is translated back and read aloud via Text-to-Speech (TTS).

## ✨ Key "X-Factors"

- **Voice-First Interface:** Zero typing required. Designed for ethnographic comfort.
- **Automated Document Intelligence:** Users can "snap" a photo of their ID; AI pre-fills 80% of the application form.
- **Eligibility Engine:** Instead of searching, users describe their life situation, and the AI matches them to relevant schemes.
- **DPDP Act Compliance:** Privacy-by-design. Audio-based consent management for low-literacy users.

## 📈 Social Impact & ROI

- **Plugging Leakages:** Aligns with India's DBT system which has saved ₹3.48 lakh crore.
- **Cost Reduction:** Reduces the "cost of documentation" which can currently exceed 150% of a rural worker's daily wage.
- **Inclusion:** Targets 115 Aspirational Districts to raise the Welfare Efficiency Index (WEI).

## 🗺️ Roadmap

- Phase 1: Pilot launch in 5 Aspirational Districts (Hindi/Marathi/Tamil).
- Phase 2: Integration of "Scene Text OCR" for handwritten local certificates.
- Phase 3: Conversational UPI integration for scheme-related payments.

## ⚖️ Compliance & Privacy

Sarkari Dost is built to be fully compliant with:

- Digital Personal Data Protection (DPDP) Act 2023
- Aadhaar Act 2016
- UIDAI Data Security Guidelines

## 👥 Contributors

- Arpit Rohila - Initial Work & Architecture

Built with ❤️ for the Digital India Vision.
