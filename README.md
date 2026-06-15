# Medicare App Backend

FastAPI backend for the Medicare appointment and doctor management system.

## Features

- **FastAPI** - High-performance async Python web framework
- **SQLAlchemy ORM** - Database abstraction and model management
- **CORS Support** - Configured for frontend integration
- **API Documentation** - Auto-generated with Swagger UI and ReDoc
- **Comprehensive API Endpoints** - Appointments, Doctors, and Patient management

## Quick Start

### Prerequisites
- Python 3.11+
- pip

### Local Development

1. **Create virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server:**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

4. **Access API documentation:**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Docker

### Build and run with Docker:

```bash
docker build -t medicare-backend .
docker run -p 8000:8000 medicare-backend
```

### Using Docker Compose:

```bash
docker-compose up backend
```

## API Endpoints

### Doctors
- `GET /api/v1/doctors` - List all doctors
- `POST /api/v1/doctors` - Create a new doctor
- `GET /api/v1/doctors/{id}` - Get doctor details

### Appointments
- `GET /api/v1/appointments` - List all appointments
- `POST /api/v1/appointments` - Book an appointment
- `GET /api/v1/appointments/{id}` - Get appointment details

### Info
- `GET /api/v1/info` - Get app information and available departments

## Testing

### Run tests:
```bash
pytest
```

### Run tests with coverage:
```bash
pytest --cov=app --cov-report=term-missing
```

### Current Coverage
- Target: 10% test coverage
- Status: In progress

## Configuration

Environment variables can be set in `.env` file:

```bash
PYTHONUNBUFFERED=1
DATABASE_URL=sqlite:///./test.db
```

## Project Structure

```
backend/
├── app/
│   ├── main.py           # FastAPI application entry point
│   ├── database.py       # Database configuration
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas for validation
│   └── routers/
│       ├── doctors.py    # Doctor endpoints
│       ├── appointments.py # Appointment endpoints
│       └── patients.py   # Patient endpoints
├── tests/                # Test suite
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
└── README.md
```

## Development Workflow

1. Create feature branches for new features
2. Implement endpoints with proper documentation
3. Add tests for new functionality
4. Update API schemas and models as needed
5. Submit pull request for review
6. Merge to main after approval

## Deployment

Both frontend and backend are containerized for easy deployment to Docker Hub.

### Build Docker image:
```bash
docker build -t <dockerhub-username>/medicare-backend:<version> .
docker push <dockerhub-username>/medicare-backend:<version>
```

See the main README for deployment instructions.
