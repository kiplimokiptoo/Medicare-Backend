# Backend

FastAPI backend for the Medicare App.

Quick start:

1. Create a virtualenv: `python -m venv .venv` then `source .venv/bin/activate`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the app: `uvicorn app.main:app --reload --port 8000`.
4. Open docs at `http://localhost:8000/docs` or `http://localhost:8000/redoc`.

Run tests and coverage:

```
pytest --maxfail=1 --disable-warnings -q
pytest --cov=app --cov-report=term-missing
```
# Backend

This folder will contain backend code (APIs, database, etc.).
