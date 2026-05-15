# GitHub Profile Analyzer

Developer analytics platform built using FastAPI, Streamlit, and GitHub APIs.

The platform analyzes GitHub profiles and generates recruiter-style insights, developer analytics, contribution statistics, and markdown-based technical resumes.

---

# Live Demo

Frontend:  
https://git-profile-analyzer-vinesh.streamlit.app

Backend API Docs:  
https://github-profile-analyzer-3vy1.onrender.com/docs

---

# Features

## AI Recruiter Analysis

Analyzes repositories and developer activity to generate:

- Recommended developer roles
- Technical strengths
- Weak areas
- Hiring insights

---

## Developer DNA

Generates developer personality insights based on repository patterns, technologies, and contribution behavior.

Examples:
- Rapid Builder
- Backend Focused
- Experimentation Driven

---

## GitHub Wrapped

Provides developer activity analytics including:

- Productivity score
- Repository statistics
- Contribution analytics
- Most productive coding hour
- Estimated active days
- Top languages used

---

## Startup Readiness Score

Evaluates engineering practices and project maturity including:

- Deployment readiness
- CI/CD adoption
- Repository structure quality
- Development workflow indicators

---

## AI Resume Generator

Generates a markdown-based technical resume using:

- GitHub repositories
- Technologies used
- Project summaries
- Profile analytics

---

# Technology Stack

## Backend

- FastAPI
- Pydantic
- Uvicorn
- Requests

## Frontend

- Streamlit
- Plotly
- Pandas

## DevOps & Tooling

- GitHub Actions
- Ruff
- Pytest
- Render
- Streamlit Community Cloud

---

# System Architecture

```text
Streamlit Frontend
        ↓
FastAPI Backend
        ↓
GitHub REST API
```

---

# Project Structure

```text
GitHub-Profile-Analyzer/
│
├── backend/
│   ├── app/
│   │   ├── analysis/
│   │   ├── api/
│   │   ├── models/
│   │   ├── services/
│   │   └── utils/
│   │
│   ├── tests/
│   └── requirements.txt
│
├── frontend/
│   ├── components/
│   ├── utils/
│   ├── app.py
│   └── requirements.txt
│
└── .github/workflows/
```

---

# Local Setup

## Clone Repository

```bash
git clone https://github.com/Vineshnayak/GitHub-Profile-Analyzer.git
```

---

# Backend Setup

```bash
cd backend

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# Frontend Setup

```bash
cd frontend

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# API Endpoints

| Endpoint | Description |
|---|---|
| `/profile/{username}` | GitHub profile analytics |
| `/resume/{username}` | Resume generation |
| `/wrapped/{username}` | GitHub Wrapped analytics |

---

# Testing

Run backend tests:

```bash
python -m pytest
```

---

# Linting

Run Ruff linter:

```bash
python -m ruff check .
```

---

# CI/CD

GitHub Actions workflow automatically runs:

- Lint checks
- Backend tests
- Dependency validation

on every push to `main`.

---

# Deployment

## Backend

Deployed using Render.

## Frontend

Deployed using Streamlit Community Cloud.

---

# Future Improvements

- PDF resume export
- Repository semantic analysis
- GitHub contribution heatmaps
- AI interview question generation
- Authentication support

---

# Author

Vinesh Nayak