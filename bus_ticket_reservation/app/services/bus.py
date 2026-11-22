from sqlalchemy.orm import Session
from app.models.bus import Bus
from app.schemas.bus import BusCreate


def create_bus(db: Session, bus: BusCreate):

    db_bus = Bus(
        **bus.model_dump(),
        available_seats=bus.total_seats
    )

    db.add(db_bus)
    db.commit()
    db.refresh(db_bus)

    return db_bus


def get_all_buses(db: Session):

    return db.query(Bus).all()


def get_bus_by_id(db: Session, bus_id: int):

    return db.query(Bus).filter(Bus.id == bus_id).first()