# Open Abuse Detector

A FastAPI-based API that classifies tweets as abusive or not using a pre-trained HuggingFace model. Includes a basic D3.js frontend to visualize results.

## Features
- `/classify` endpoint for abuse detection.
- Basic D3.js visualization for analysis.
- Dockerized for easy deployment.

## Getting Started

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
Open `frontend/index.html` in your browser.

### Docker
```bash
docker build -t abuse-detector .
docker run -p 8000:8000 abuse-detector
```
