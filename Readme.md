# 🏛️ Sarkari Dost (Government Friend)

**Bridging the Last Mile between Government Schemes and Global Citizens**

Sarkari Dost is an AI-powered **conversational bridge** designed to eradicate the digital and linguistic divide in India. It transforms complex, English-centric government portals into simple, voice-based experiences in regional dialects, targeting the **Next Billion** users.

---

## 🚀 The Vision

Over **250 million rural citizens** are eligible for government welfare but fail to apply due to:

- **Information Asymmetry:** Legal and bureaucratic language is difficult to interpret.
- **Linguistic Barriers:** Most portals support only English or formal Hindi.
- **Form Anxiety:** Fear of making mistakes on official documents.

Sarkari Dost acts as a **localized mediator**, using voice-first AI to make **Digital Public Infrastructure (DPI)** accessible to everyone—regardless of literacy level or language.

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|------|-----------|---------|
| Frontend | React (SPA) / PWA | High performance on low-end devices, offline caching |
| Voice & NLP | Bhashini APIs | ASR, TTS, NMT for 22+ Indian languages |
| Brain (LLM) | Llama 3.3 (via Groq) | Ultra-low latency real-time reasoning |
| RAG Pipeline | LangChain + Pinecone | Hallucination-free retrieval from verified sources |
| OCR | Google Vision / IIIT-H | Data extraction from physical ID cards |
| Backend | FastAPI + Supabase | Scalable, async voice-stream processing |

---

## 🏗️ Technical Architecture: Agentic RAG

Sarkari Dost follows a **Sense → Reason → Act** architecture to ensure reliability, speed, and trust.

### Flow Overview

1. **Ingestion**
   - Firecrawl scrapes portals like `myScheme.gov.in`
   - Data cleaned and structured into JSON

2. **Indexing**
   - Scheme data chunked and embedded
   - Stored in Pinecone Vector Database

3. **User Request**
   - Citizen asks a question in a regional dialect via voice

4. **Translation**
   - Bhashini converts Voice → Local Text → English

5. **Reasoning**
   - LLM retrieves relevant schemes
   - Eligibility is inferred
   - Simple summary is synthesized

6. **Response**
   - Answer translated back
   - Spoken aloud via Bhashini TTS

---

## 🧠 System Diagram (Logical Flow)

            ┌──────────────┐
            │ Citizen      │
            │ (Voice Input)│
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │ Bhashini     │ ASR / NMT
            │ (Speech → EN)│
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │ Agentic RAG  │
            │ Orchestrator │
            │ (LangChain)  │
            └──────┬───────┘
                   │ Retrieve
                   ▼
┌──────────────┐      ┌─────────────┐
│ Vector DB    │◄────►│  LLM (Groq) │
│ (Schemes)    │      │   Llama 3.3 │
└──────┬───────┘      └─────┬───────┘
       │ Synthesized Answer │
       └──────────────┬─────┘
                      ▼
               ┌──────────────┐
               │ Bhashini     │ TTS
               │ (EN → Local) │
               └──────┬───────┘
                      ▼
                ┌──────────────┐
                │ Citizen      │
                │ (Voice Out)  │
                └──────────────┘


---

## ✨ Key X-Factors

- **Voice-First Interface:** Zero typing; ethnographic conversational design
- **Automated Document Intelligence:** OCR-based pre-fill covers ~80% of form fields
- **Eligibility Engine:** Users describe life situations; AI matches schemes
- **Privacy-by-Design:** Voice-based consent aligned with DPDP Act 2023

---

## 🧩 Problem → Solution Mapping

| Problem | Ground Reality | Sarkari Dost Solution | Impact |
|-------|----------------|----------------------|--------|
| Information Asymmetry | Users don’t know relevant schemes | Context-aware conversational retrieval | Higher enrollment |
| Language Exclusion | English/Formal Hindi portals | Dialect-aware voice interaction | Inclusive access |
| Form Anxiety | Fear of errors | Guided voice flows + OCR | User confidence |
| Middlemen Dependency | 10–20% commission loss | Direct-to-citizen access | Reduced leakage |
| Low Digital Literacy | Text-heavy UX | Voice-first design | Accessibility |

---

## 📈 Social Impact & ROI

- **Plugging Leakages:** Aligns with DBT savings of ₹3.48 lakh crore
- **Cost Reduction:** Cuts documentation cost exceeding 150% of daily rural wages
- **Inclusion:** Targets 115 Aspirational Districts to raise Welfare Efficiency Index (WEI)

---

## ⏱️ Why Now?

### 1. DPI Maturity
Aadhaar, UPI, DigiLocker, and DBT are at population scale. The missing layer is **usability**.

### 2. National Language AI Stack
**Bhashini** enables sovereign, Indic-language conversational AI for the first time.

### 3. Reliable LLM + RAG
Modern RAG architectures ensure **deterministic, explainable outputs**—critical for governance.

### 4. Policy Readiness
The **DPDP Act 2023** provides clear guardrails for privacy-first GovTech innovation.

---

## ⚠️ Risks & Mitigation

| Risk | Mitigation |
|-----|-----------|
| LLM Hallucination | Strict RAG grounding |
| Dialect Ambiguity | Bhashini fine-tuning |
| Data Misuse | Ephemeral processing |
| Adoption Resistance | CSC-assisted onboarding |
| Regulatory Changes | Modular compliance layer |

---

## ⚖️ Compliance & Privacy

Fully compliant with:
- Digital Personal Data Protection (DPDP) Act 2023
- Aadhaar Act 2016
- UIDAI Data Security Guidelines

---

## 👥 Contributors

- **Arpit Rohila** – Initial Architecture & Concept
- **Kartikey Nautiyal** - Data Collection & Chunking 
---

## 🏁 Closing Note

**Sarkari Dost** is not just an application—it is an **accessibility layer for democracy**.

When citizens can speak in their own language, understand their rights, and act without fear, governance becomes truly inclusive.

> *Your language should never be a barrier to your rights.*
