# Medicare Backend

FastAPI backend that provides department data for the Medicare frontend.

Run locally:

```bash
python -m pip install -r backend/requirements.txt
uvicorn backend.main:app --reload --port 8000
```

API endpoints:

- `GET /` - health message
- `GET /departments` - list of departments
