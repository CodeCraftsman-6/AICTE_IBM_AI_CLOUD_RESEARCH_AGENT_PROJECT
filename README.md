# Research Agent 🧠📚
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

## 🔍 Overview

**Research Agent** is an AI-powered academic assistant that simplifies the research process. It provides tools for semantic search, paper summarization, citation analysis, trend detection, and author collaboration mapping. Designed for students, researchers, and scholars to boost productivity and insight in literature review and exploration.

---

## ✨ Key Features

- 🔎 **Semantic Search** – Search research papers using natural language queries.
- 🧾 **Auto-Summarization** – Generate short summaries of academic papers.
- 📈 **Trend Analysis** – Identify emerging topics in your field of interest.
- 🔗 **Citation Analysis** – Assess the influence of papers using citation data.
- 🧠 **Recommendation System** – Discover relevant and related research.
- 👥 **Collaboration Mapping** – Visualize networks between researchers/institutions.
- ⚙️ **Deployment** – Easily deployable via IBM Watsonx GPT Runtime or locally.

---

## 🧰 Technologies Used

- **Language**: Python 3.10+
- **Libraries**:
  - `transformers`, `langchain` – NLP and AI
  - `pandas`, `numpy`, `matplotlib` – Data handling and visualization
  - `scikit-learn` – Machine learning models
- **APIs**:
  - [OpenAI GPT](https://platform.openai.com/)
  - [Semantic Scholar](https://api.semanticscholar.org/)
- **Deployment**:
  - IBM Watsonx GPT Runtime
  - Optional: Docker, Flask/FastAPI

---

## ⚙️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ResearchAgent.git
   cd ResearchAgent
#Set Up a Virtual Environment (recommended):
   python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

#Install Required Packages:
   pip install -r requirements.txt

#Configure API Keys:
Create a .env file in the root directory:
OPENAI_API_KEY=your_openai_key
SEMANTIC_SCHOLAR_API_KEY=your_semantic_scholar_key

---

🚀 Getting Started
Run from CLI:
python src/main.py

Example Command:
> What are the recent breakthroughs in quantum machine learning?

Planned Web Interface:
Web version using Flask or Streamlit is in progress.

---

🗂 Project Structure:

ResearchAgent/
│
├── data/                     # Sample or processed data
├── models/                   # Pre-trained or custom ML models
├── src/                      # Core logic
│   ├── semantic_search.py
│   ├── summarization.py
│   ├── citation_analysis.py
│   ├── trend_analysis.py
│   ├── recommendations.py
│   ├── collaboration_map.py
│   └── main.py               # Entry point
│
├── .env                      # API Keys (not included in repo)
├── requirements.txt
├── LICENSE
└── README.md

---

🌱 Future Enhancements
-> Add ArXiv and PubMed support

-> Collaborative filtering in recommendations

-> Streamlit web app for easy interaction

-> Paper upload and parsing (PDF reader)

---

🙏 Acknowledgements
-> OpenAI

-> Semantic Scholar

-> HuggingFace Transformers, Langchain, Scikit-learn

-> IBM Watsonx GPT Runtime

---





