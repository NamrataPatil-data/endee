# 🚀 AI Skill Gap Analyzer (RAG + Endee Inspired)

## 📌 Overview
This project is an AI-based Skill Gap Analyzer that compares a user's resume with a job description and identifies missing skills.

It uses RAG (Retrieval-Augmented Generation) for semantic search and is designed to integrate with the Endee Vector Database.

## 🧠 Features
- Resume vs Job Description comparison
- Semantic similarity using embeddings
- Top-K relevant skills ranking
- Match score calculation
- Missing skills identification
- AI-based insights

## ⚙️ Tech Stack
- Python
- Streamlit
- Sentence Transformers
- PDFPlumber

## 🔍 RAG Implementation
- Convert text into embeddings
- Perform semantic similarity search
- Retrieve top-K relevant skills

## 🗄️ Endee Integration
This project is designed to integrate with the Endee vector database. Currently, it uses local embeddings.

## ▶️ Run
pip install -r requirements.txt  
streamlit run app.py

## 🚀 Future Work
- Integration with Endee database using Docker
