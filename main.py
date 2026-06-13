from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Medicare Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

departments = [
    {
        "id": "cardiology",
        "name": "Cardiology",
        "desc": "Heart and vascular diseases, advanced interventions.",
        "img": "https://images.unsplash.com/photo-1580281657521-6f4b2b7bd0d8?auto=format&fit=crop&w=800&q=60",
    },
    {
        "id": "neurology",
        "name": "Neurology",
        "desc": "Stroke, epilepsy, migraine, and Parkinson's care.",
        "img": "https://images.unsplash.com/photo-1586773860416-7c0f5cb5f0a0?auto=format&fit=crop&w=800&q=60",
    },
    {
        "id": "orthopedics",
        "name": "Orthopedics",
        "desc": "Joint replacement, sports injuries, and spine surgery.",
        "img": "https://images.unsplash.com/photo-1584467735875-2d5f0e5b1a6b?auto=format&fit=crop&w=800&q=60",
    },
    {
        "id": "pediatrics",
        "name": "Pediatrics",
        "desc": "Child health, vaccinations, and developmental care.",
        "img": "https://images.unsplash.com/photo-1584466977778-7f3f6b6f9d1b?auto=format&fit=crop&w=800&q=60",
    },
    {
        "id": "dermatology",
        "name": "Dermatology",
        "desc": "Skin disorders, laser treatments, and acne care.",
        "img": "https://images.unsplash.com/photo-1526256262350-7da7584cf5eb?auto=format&fit=crop&w=800&q=60",
    },
    {
        "id": "gynecology",
        "name": "Gynecology",
        "desc": "Women's health, maternity, and fertility services.",
        "img": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=800&q=60",
    },
    {
        "id": "dentist",
        "name": "Dentist",
        "desc": "Dental implants, braces, root canals, and oral hygiene.",
        "img": "https://images.unsplash.com/photo-1588774069150-1b3d9b8b7f7e?auto=format&fit=crop&w=800&q=60",
    },
    {
        "id": "eye",
        "name": "Eye Center",
        "desc": "Cataract surgery, LASIK, glaucoma treatment, and vision therapy.",
        "img": "https://images.unsplash.com/photo-1526256262350-7da7584cf5eb?auto=format&fit=crop&w=800&q=60",
    },
]


@app.get("/", tags=["root"])
async def root():
    return {"message": "Medicare backend is running"}


@app.get("/departments", tags=["departments"])
async def list_departments():
    return {"count": len(departments), "results": departments}
