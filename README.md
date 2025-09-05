Mini-Lab — Local Full-Stack Starter (FastAPI + Next.js)

This project is a full-stack starter I set up locally using FastAPI for the backend and Next.js for the frontend.
It's meant to be a reusable starting point for assignments. It includes:

✅ /api/health endpoint (FastAPI) returning { "status": "ok" }

✅ A frontend page that fetches and displays the API status live

✅ Local-only setup (no cloud services)

✅ Basic API key safety with .env.example

Backend Setup (FastAPI)
Requirements

Python 3.11+

pip

Setup Steps
Go to the backend folder

cd backend

Create and activate a virtual environment

python -m venv .venv
source .venv/bin/activate

Install dependencies

pip install -r requirements.txt

Run the FastAPI dev server

uvicorn app.main:app --reload

Visit the backend health check at:
http://localhost:8000/api/health

Frontend Setup (Next.js)
Requirements

Node.js 18+

npm (comes with Node)

Setup Steps
Go to the frontend folder

cd ../frontend

Install Node dependencies

npm install

Start the dev server

npm run dev

Visit the frontend health page at:
http://localhost:3000/health-status

🔐 API Keys and Environment

If this app ever uses secrets (like an API key), they should go in a .env file.

A .env.example file is included in both the root and frontend folders.

Never commit real secrets.

The frontend displays an “AI Disabled” banner if any required key is missing (placeholder only for now).

Optional: Docker Setup

You don’t need Docker to run this, but here’s a sample setup if you want it:

docker compose up --build

Make sure you have Docker and Docker Compose installed.

✅ Dev QA (Checklist)
Check	Status
/api/health returns JSON 200	✅
Frontend fetches & shows status	✅
No console or terminal errors	✅
🖼️ Proof of Working Setup

Screenshots are saved in the /docs folder and include:

✅ Backend terminal running FastAPI

✅ Frontend terminal running Next.js

✅ http://localhost:8000

✅ http://localhost:8000/api/health

✅ http://localhost:3000

✅ http://localhost:3000/health-status

GitHub Copilot Use

I used GitHub Copilot to scaffold parts of this project.

✅ Accepted Prompt:
"Create a FastAPI route /api/health that returns {status: 'ok'} and enable CORS for http://localhost:3000
"
✔️ I accepted it. It generated the exact endpoint and CORS setup I needed.

❌ Rejected Prompt:
"Generate full CRUD with database connection"
❌ I rejected this. It was too advanced for this week’s scope and not required.