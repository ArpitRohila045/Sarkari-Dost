# 🏛️ Sarkari Dost – AI-Powered Conversational GovTech Platform

**Tagline:** Bridging the Last Mile between Government Schemes and Citizens  

Sarkari Dost is a **voice-first, multilingual conversational platform** that enables citizens—especially rural and non-English speakers—to discover, understand, and apply for government welfare schemes through natural dialogue instead of complex portals and forms.

---

## 🎯 Problem Statement

Millions of eligible citizens fail to access welfare schemes due to:
- English-centric and text-heavy government portals
- Low digital literacy and regional dialect diversity
- Lack of awareness of applicable schemes
- Fear of making mistakes on official forms (“form anxiety”)
- Dependency on intermediaries charging high commissions

Sarkari Dost replaces **search and forms** with **guided conversation** in the user’s own language.

---

## 🌍 Vision

To act as a **conversational access layer** over India’s Digital Public Infrastructure (DPI), ensuring that **language, literacy, or technology never become barriers to citizens’ rights**.

---

## 
## 🧭 End-to-End Workflow Overview
![Diagram](diagram_design/DataBase_FlowChart_Design.jpg)
---

## 🗣️ Detailed Application Flow

### 1️⃣ Voice-Based User Interaction
- User speaks naturally in a regional language or dialect  
  Example: *“pension ke baare mein batao”*
- No scheme names, keywords, or typing required

---

### 2️⃣ Speech Processing (ASR)
- Frontend records audio
- **Bhashini ASR** converts speech → text
- Language and dialect automatically detected

**Why Bhashini:**  
Government-backed, Indic-language optimized, sovereign AI stack

---

### 3️⃣ Session & Context Loading
- Backend loads session context from **Redis**
- Retrieves:
  - Current intent
  - Active scheme (if any)
  - Known user attributes (age, income, state, etc.)
  - Conversation summary

**Design Principle:**  
No raw chat history — only structured meaning.

---

### 4️⃣ Intent Detection & Information Gap Analysis
The system classifies intent:
- Scheme discovery
- Benefit query
- Eligibility check
- Document requirement
- Follow-up
- Context switch

For example, pension-related queries require:
- Age
- Income
- State
- (Optional) Marital status

The system computes:
---

### 5️⃣ Progressive Slot-Filling (If Info Is Missing)
Instead of guessing, the system asks **one question at a time**.

Example:
> “Aapki umar kya hai?”

- User answers via voice
- Attribute stored in session profile
- System re-evaluates missing information

**UX Principle:**  
Ask only what reduces uncertainty the most.

---

### 6️⃣ Retrieval-Augmented Generation (RAG)
Triggered only when sufficient information is available.

Steps:
- Query + user profile embedded
- Semantic search in **Vector DB (Pinecone)**
- Retrieves relevant scheme documents
- Filters by state, category, eligibility

**Why RAG:**  
Ensures policy-grounded, hallucination-free responses.

---

### 7️⃣ Context-Aware LLM Reasoning
- LLM (Llama 3.3) receives:
  - Retrieved scheme text
  - User profile summary
  - Active scheme
  - Conversation context
- Generates:
  - Scheme explanation
  - Benefits
  - Eligibility conditions
  - Next steps
  - Required documents

**Important:**  
LLM explains facts; eligibility logic remains deterministic.

---

### 8️⃣ Voice Response Generation
- Answer translated back into user’s language
- **Bhashini TTS** converts text → speech
- Voice response delivered to user

**Accessibility Win:**  
Even illiterate users receive full guidance.

---

### 9️⃣ Context Update & Optimization
- Redis session updated with:
  - Active scheme
  - Conversation summary
  - Updated user attributes
- TTL refreshed (default: 30 minutes)

Example follow-up:
> “Isme kitna paisa milega?”

➡️ Answered instantly without re-running retrieval.

---

## 🧠 Conversation Intelligence Design

### Structured Conversation State (Not Chat Logs)
```json
{
  "current_intent": "pension_query",
  "active_scheme": "IGNOAPS",
  "conversation_summary": "User asked about pension eligibility",
  "user_profile": { "age": 65, "state": "UP" }
}
