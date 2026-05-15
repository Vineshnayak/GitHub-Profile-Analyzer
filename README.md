# GitHub Profile Analyzer

A full-stack developer analytics platform that analyzes GitHub profiles and generates professional developer insights using GitHub APIs, FastAPI, Streamlit, and DevOps workflows.

---

## Live Demo

### Frontend
https://git-profile-analyzer-vinesh.streamlit.app

### Backend API Docs
https://github-profile-analyzer-3vy1.onrender.com/docs

---

## Features

- GitHub profile analysis
- Repository analytics
- Language usage statistics
- Developer scoring system
- Tech stack extraction
- Repository statistics
- Interactive dashboard
- API-based architecture
- CI/CD pipelines using GitHub Actions
- Production deployment

---

## Tech Stack

### Backend
- Python
- FastAPI
- Requests

### Frontend
- Streamlit
- Pandas

### DevOps
- GitHub Actions
- Render
- Streamlit Cloud

---

## Architecture

Frontend (Streamlit)
        ↓
Backend API (FastAPI)
        ↓
GitHub REST API

---

## Project Structure

```text
GitHub-Profile-Analyzer/
│
├── backend/
│   ├── app/
│   │   ├── analysis/
│   │   ├── api/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── .github/
│   └── workflows/
│
└── README.md