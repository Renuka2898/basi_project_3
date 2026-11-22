from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.bus import BusCreate, BusResponse
from app.services import bus as bus_service

router = APIRouter(
    prefix="/buses",
    tags=["Bus Management"]
)


# CREATE BUS
@router.post("/", response_model=BusResponse)
def create_bus(
    bus: BusCreate,
    db: Session = Depends(get_db)
):
    return bus_service.create_bus(db, bus)


# GET ALL BUSES
@router.get("/", response_model=list[BusResponse])
def get_all_buses(db: Session = Depends(get_db)):
    return bus_service.get_all_buses(db)


# GET BUS BY ID
@router.get("/{bus_id}", response_model=BusResponse)
def get_bus(
    bus_id: int,
    db: Session = Depends(get_db)
):
    bus = bus_service.get_bus_by_id(db, bus_id)

    if bus is None:
        raise HTTPException(status_code=404, detail="Bus not found")

    return bus