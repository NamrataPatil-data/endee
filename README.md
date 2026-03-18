# 🚀 AI Skill Gap Analyzer (RAG + Endee Inspired)

## 📌 Overview

This project is an AI-based Skill Gap Analyzer that compares a user's resume with a job description and identifies missing skills.

It uses **RAG (Retrieval-Augmented Generation)** for semantic search and follows a vector-search-based architecture inspired by the Endee Vector Database.

## 💡 Features

* Resume vs Job Description comparison
* Semantic similarity using embeddings
* Top-K relevant skills ranking
* Match score calculation
* Missing skills identification
* AI-based insights

## ⚙️ Tech Stack

* Python
* Streamlit
* Sentence Transformers
* PDFPlumber

## 🔍 RAG Implementation

* Convert text into embeddings
* Perform semantic similarity search
* Retrieve Top-K relevant skills

👉 The system retrieves **Top-K most relevant skills** based on cosine similarity between embeddings.

## 🧠 Endee Integration

This project uses a vector-search-based architecture inspired by the **Endee Vector Database** for semantic search and skill ranking.

Currently, it uses local embeddings, and it is designed to integrate with Endee for scalable vector search.

## ▶️ Run the Project

bash
pip install -r requirements.txt
streamlit run app.py

## 🔮 Future Work

* Integration with Endee database using Docker
* Real-time vector search using Endee APIs
* Advanced RAG pipelines
