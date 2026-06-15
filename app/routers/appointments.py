from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.Appointment])
def list_appointments(db: Session = Depends(get_db)):
    """Get all appointments"""
    return db.query(models.Appointment).all()

@router.post("/", response_model=schemas.Appointment)
def create_appointment(payload: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    """Create a new appointment"""
    appt = models.Appointment(**payload.dict())
    db.add(appt)
    db.commit()
    db.refresh(appt)
    return appt

@router.get("/{appointment_id}", response_model=schemas.Appointment)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    """Get a specific appointment"""
    appt = db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
    if not appt:
        raise ValueError("Appointment not found")
    return appt
