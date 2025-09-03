# Free AI Customer Support Assistant

An **end-to-end customer support assistant** built entirely with **open-source AI models**.  
This project demonstrates how Large Language Models (LLMs) can be integrated with retrieval techniques to answer customer FAQs reliably — without relying on commercial APIs.

---

## ✨ Project Highlights

- **LLM Backbone**: [Google FLAN-T5-base](https://huggingface.co/google/flan-t5-base), a free and instruction-tuned text-to-text model, hosted on Hugging Face.
- **Retrieval-Augmented Generation (RAG)**:
  - FAQ documents embedded with **Sentence Transformers**.
  - Vector similarity search using **FAISS**.
- **Governance & Safety**: Explicit _“I don’t know”_ fallback for questions outside the knowledge base.
- **Deployment**: Lightweight **Streamlit** app for interactive demonstration.
- **No Paid APIs**: 100% free and reproducible using open models.

---

## 📂 Repository Structure

```

.
├── app/
│   └── app.py              # Streamlit front-end
├── core/
│   ├── retriever.py        # FAISS retriever for context lookup
│   └── generator.py        # FLAN-T5 text generator with safeguards
├── data/
│   └── faq.json            # Example FAQ dataset
├── requirements.txt        # Dependencies
└── README.md               # This file

```

---

## ⚙️ Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/customer-support-assistant.git
   cd customer-support-assistant
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:

   ```bash
   streamlit run app/app.py
   ```

---

## 🎯 Usage

1. Enter a customer query (e.g., _“What is your return policy?”_).
2. The system:

   - Retrieves the most relevant FAQ entry using FAISS.
   - Passes both the query and context to FLAN-T5 for answer generation.
   - Returns an answer grounded in the FAQ, or a safe fallback if not covered.

Example:

**Query**: _What is your return policy?_
**Context**: _You can return items within 30 days of purchase._
**Answer**: _You can return items within 30 days of purchase._

---

## 🧠 Skills Demonstrated

- **Natural Language Processing**: Prompt engineering, retrieval-augmented generation.
- **Open-Source LLMs**: Deployment of Hugging Face models without proprietary APIs.
- **Vector Search**: FAISS integration for semantic similarity.
- **MLOps Lite**: Modular codebase, clear separation of retriever vs. generator.
- **Responsible AI**: Safeguards against hallucination; explicit fallback responses.
- **Interactive Deployment**: Streamlit-based demo showcasing end-user experience.

---

## 📊 Why This Project Matters

- **Business Value**: Reduces cost of customer support, improves consistency, scales instantly.
- **Hiring Value**: Shows capability to architect AI systems that are _practical_, _deployable_, and _ethically aligned_.
- **Future Extensions**:

  - Fine-tuning FLAN-T5 on domain-specific data.
  - Adding multi-turn dialogue with memory.
  - Deploying as an API service via FastAPI or Docker.
  - Integrating analytics dashboards for usage monitoring.

---

## 🚀 Demo

Run locally with Streamlit:

```bash
streamlit run app/app.py
```

Sample browser interface:

```
Free AI Customer Support Assistant
Type a question related to the FAQ and press Enter.
```

---

## 📖 References

- [Google Research: FLAN-T5](https://arxiv.org/abs/2210.11416)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [FAISS: Facebook AI Similarity Search](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)

---

## 👤 Author

**Athar Kharal, PhD**
Data Scientist | AI-Augmented Workflows | Technical Documentation Systems

- PhD in Computational Mathematics
- Expertise: LLMs, Data Science, Technical Writing, MLOps

---

## ⚠️ Disclaimer

This assistant is a **demonstration project**.
The responses are limited to the FAQ data provided. It is **not** intended for production use without additional safeguards, evaluation, and scaling.
