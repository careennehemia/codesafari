# CodeSafari 101

**Your One-Stop Coding Adventure** - A self-guided programming platform inspired by MIT's rigorous computer science curriculum, featuring AI-powered assistance with RAG technology.

## Features

- **Skills-Based Learning**: Choose from Python, JavaScript, C Programming, and Web Development tracks
- **AI Tutor**: GPT-4 powered chatbot that only answers lab-related questions (RAG-filtered)

## Architecture

- **Frontend**: React + TypeScript + Custom CSS (Port 3001)
- **Backend**: FastAPI + Python (Port 8000)
- **AI**: OpenAI GPT-4 with keyword-based RAG filtering
- **Database**: In-memory lab content storage

## Quick Start

### 1. Setup Backend (FastAPI)
```bash
cd backend
source venv/bin/activate  # Virtual environment is already created
# Add your OpenAI API key to backend/.env:
# OPENAI_API_KEY=your_actual_openai_api_key_here
```

### 2. Setup Frontend (React)
```bash
# Frontend is already running on port 3001
# Visit: http://localhost:3001
```

### 3. Test the Platform
1. **Browse Skills**: Click on Python, JavaScript, C, or Web Development
2. **Select a Lab**: Click "Start Lab" on any lab card
3. **Read Content**: Review the reading material and exercises
4. **Ask AI Questions**: Use the chatbot to get help (only lab-related questions work!)

##  Sample Lab Questions to Try

**For Python BFS Lab:**
- "How does BFS work?"
- "What's the difference between BFS and DFS?"
- "How do I implement a queue in Python?"

**For JavaScript Lab:**
- "What are arrow functions?"
- "How do I use async/await?"
- "Explain event handling in JavaScript"

**Non-Lab Questions (Will be filtered out):**
- "Who is Rihanna?" 
- "What's the weather like?" 

## Project Structure

```
codesafari-101/
├── src/                    # React frontend
│   ├── components/
│   │   ├── ChatBot.tsx     # AI chatbot component
│   │   └── LabDetail.tsx   # Lab content display
│   ├── App.tsx             # Main application
│   └── App.css             # Custom styling
├── backend/                # FastAPI backend
│   ├── main.py             # API server with GPT + RAG
│   ├── requirements.txt    # Python dependencies
│   └── .env                # OpenAI API key (add yours!)
└── README.md               # This file
```

