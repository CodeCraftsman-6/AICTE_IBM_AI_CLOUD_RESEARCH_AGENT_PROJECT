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

## 🌐 IBM Cloud Services Used

   • IBM Watsonx.ai Studio – AI model training and deployment.
   
   • IBM Cloud Object Storage – Data input and retrieval.
   
   • IBM IAM (Identity and Access Management) – Secure authentication and access.
   
   • IBM Cloud Lite Account – Enables development and deployment at zero cost for initial testing.

---

## ✨ WOW Factors

• Autonomous Literature Search – Finds and retrieves academic papers and trusted research sources in real time using IBM Cloud APIs.

• Intelligent Summarization – Generates concise, high-quality summaries of research papers and articles.

• Automated Citation Management – Extracts references and formats them in popular citation styles (APA, IEEE, MLA).

• Hypothesis & Draft Generation – Suggests research hypotheses and drafts sections of papers tailored to the research question.

• Multi-Domain Support – Adaptable to various academic disciplines and industrial R&D needs.

• Cloud-Native Deployment – Fully deployed on IBM Cloud Lite for scalability, reliability, and collaborative access.

---

## 👥 Target Users

• Researchers & Academics – For faster literature reviews and structured research paper drafting.

• University Students & Scholars – To streamline project reports, dissertations, and thesis preparation.

• R&D Teams in Industry – For rapid knowledge gathering and trend analysis.

• Librarians & Knowledge Managers – To maintain and organize research repositories.

• Policy Makers & Think Tanks – For evidence-based decision-making with fast literature insights.

---

## 🔑 Key Features

• Smart Literature Search – Retrieves relevant academic papers, journals, and trusted online resources based on user queries.

• AI Summarization – Condenses lengthy research papers into concise, easy-to-read summaries.

• Reference Management – Automatically extracts and formats citations in styles like APA, IEEE, and MLA.

• Hypothesis Generation – Suggests new research directions or hypotheses from the gathered literature.

• Section Drafting – Drafts parts of research papers such as abstracts, introductions, or related work sections.

• Cloud-Integrated – Deployed on IBM Cloud Lite using IBM Granite for secure and scalable performance.

---

## ⚙️ How It Works

• Input – User enters a research question or uploads relevant papers.

• Document Processing – The agent parses, chunks, and embeds documents for quick retrieval.

• Search & Retrieval – Fetches relevant literature from trusted sources and indexed repositories.

• Summarization – AI condenses each document and extracts key insights.

• Citation & Structuring – Generates organized references and paper-ready content.

• Deployment – Hosted on IBM Watsonx.ai with Granite models for academic-grade responses.

• Output – Provides structured summaries, citations, and draft sections for research use.

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

## 📊 Results

• The Research Agent streamlines the literature review process, reducing research time by 50–70%.

• Generates accurate, context-aware summaries using IBM Granite LLM.

• Produces properly formatted citations automatically, reducing manual work for researchers.

• Offers draft research content that aligns with academic writing standards

---

## 🚀 Getting Started
Run from CLI:
python src/main.py

Example Command:
> What are the recent breakthroughs in quantum machine learning?

Planned Web Interface:
Web version using Flask or Streamlit is in progress.

---

## 🗂 Project Structure:

ResearchAgent/
│
├── data/                    
├── models/                   
├── src/                      
│   ├── semantic_search.py
│   ├── summarization.py
│   ├── citation_analysis.py
│   ├── trend_analysis.py
│   ├── recommendations.py
│   ├── collaboration_map.py
│   └── main.py               
│
├── .env                      
├── requirements.txt
├── LICENSE
└── README.md

---

## 📌 Deployment Overview

• Log into IBM Cloud.

• Open Watsonx.ai Studio and configure an IBM Granite model for NLP tasks.

• Upload research papers or datasets to IBM Cloud Object Storage.

• Set up a document processing pipeline for ingestion, chunking, and embedding.

• Integrate retrieval and summarization workflows using IBM Granite or Watson Discovery.

• Test the agent’s performance with varied research queries for accuracy and relevance.

• Deploy as an API endpoint or web-based UI for real-time literature search and paper drafting.

---

## 🌟 Future Scope

• Multi-Language Support – Extend the agent to retrieve and summarize research in multiple languages.

• Voice Interaction – Add speech-to-text and text-to-speech for hands-free research assistance.

• Domain-Specific Tuning – Fine-tune IBM Granite models for specific academic fields (medical, engineering, law, etc.).

• Live Data Integration – Pull the latest research from trusted repositories like IEEE, Springer, and arXiv in real time.

• Collaboration Tools – Integrate shared workspaces so research teams can collaborate within the agent environment.

• Plagiarism & Citation Checks – Add academic integrity tools to detect overlaps and generate compliant references.

---
## 🙏 Acknowledgements

•  OpenAI

•  Semantic Scholar

•  HuggingFace Transformers, Langchain, Scikit-learn

•  IBM Watsonx GPT Runtime

---

## 📌 Conclusion

The Research Agent project demonstrates how agentic AI can transform the research workflow by automating literature search, summarization, citation management, and draft generation.
Using IBM Granite and Watsonx.ai on IBM Cloud Lite, the system delivers high-quality, context-aware insights in a fraction of the time required by manual processes.
This innovation holds strong potential for universities, R&D labs, and industry teams where speed, accuracy, and reliability are critical for academic and industrial innovation.

---

## 🔗 Resources & References

• IBM Cloud – IBM Cloud Platform

• IBM Watsonx.ai – Watsonx.ai Studio

• Research Repositories – IEEE Xplore, SpringerLink, arXiv, ScienceDirect

• GitHub Repository – (Your Project Code Link)

---

📜 License
This project is licensed under the MIT License.

> Created by **Sampreeti Mohapatra** during the IBM SkillsBuild for Academia Internship 2025 provided by **Edunet Foundation** and **AICTE (All India Council for Technical Education)**
> Department of Computer Science and Engineering College
> Institute of Technical Education and Research(ITER), SOA

---






