from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.Doctor])
def list_doctors(db: Session = Depends(get_db)):
    """Get all doctors"""
    return db.query(models.Doctor).all()

@router.post("/", response_model=schemas.Doctor)
def create_doctor(payload: schemas.DoctorCreate, db: Session = Depends(get_db)):
    """Create a new doctor"""
    doc = models.Doctor(**payload.dict())
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

@router.get("/{doctor_id}", response_model=schemas.Doctor)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    """Get a specific doctor"""
    doc = db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
    if not doc:
        raise ValueError("Doctor not found")
    return doc
