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

```text
Frontend (Streamlit)
        ↓
Backend API (FastAPI)
        ↓
GitHub REST API
```

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
```

---

# Local Setup

## Clone Repository

```bash
git clone https://github.com/Vineshnayak/github-profile-analyzer.git
```

---

## Backend Setup

```bash
cd backend

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Frontend Setup

```bash
cd frontend

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

---

# GitHub Actions CI/CD

This project includes:

- Automated backend testing
- Linting workflows
- CI pipelines
- Deployment-ready workflows

---

# Future Enhancements

- Contribution graph analysis
- Commit frequency analytics
- AI-based developer recommendations
- Resume generation
- Skill benchmarking
- GitHub trend analysis

---

# Author

## Vinesh nayak