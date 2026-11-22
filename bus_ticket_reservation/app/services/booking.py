from sqlalchemy.orm import Session
from app.models.bus import Bus
from app.models.booking import Booking
from app.schemas.booking import BookingCreate


def book_ticket(db: Session, booking: BookingCreate):

    bus = db.query(Bus).filter(
        Bus.id == booking.bus_id
    ).first()

    if bus is None:
        raise ValueError("Bus not found")

    if bus.available_seats < booking.seats_booked:
        raise ValueError("Not enough seats available")

    bus.available_seats -= booking.seats_booked

    db_booking = Booking(**booking.model_dump())

    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)

    return db_booking


def get_all_bookings(db: Session):

    return db.query(Booking).all()


def get_booking_by_id(db: Session, booking_id: int):

    return db.query(Booking).filter(
        Booking.id == booking_id
    ).first()


def cancel_booking(db: Session, booking_id: int):

    booking = get_booking_by_id(db, booking_id)

    if booking is None:
        raise ValueError("Booking not found")

    if booking.status == "cancelled":
        raise ValueError("Booking already cancelled")

    bus = db.query(Bus).filter(
        Bus.id == booking.bus_id
    ).first()

    if bus is None:
        raise ValueError("Associated bus not found")

    bus.available_seats += booking.seats_booked
    booking.status = "cancelled"

    db.commit()
    db.refresh(booking)

    return booking