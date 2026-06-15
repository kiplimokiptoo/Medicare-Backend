from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import appointments, doctors

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Medicare App API", 
    version="0.1.0",
    description="API for Medicare appointment and doctor management"
)

# Configure CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(appointments.router, prefix="/api/v1/appointments", tags=["appointments"])
app.include_router(doctors.router, prefix="/api/v1/doctors", tags=["doctors"])

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/", tags=["root"])
async def read_root():
    return {
        "app": "Medicare App", 
        "message": "Welcome to Medicare App API",
        "version": "0.1.0"
    }

@app.get("/api/v1/info", tags=["info"])
async def info():
    return {
        "name": "Medicare App",
        "services": ["Emergency", "Outpatient", "Inpatient"],
        "departments": [
            "Cardiology",
            "Neurology", 
            "General Practice",
            "Orthopedics",
            "Ophthalmology",
            "Emergency Medicine"
        ]
    }
