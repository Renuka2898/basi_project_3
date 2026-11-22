from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.booking import BookingCreate, BookingResponse
from app.services import booking as booking_service

router = APIRouter(
    prefix="/bookings",
    tags=["Ticket Booking"]
)


# BOOK TICKET
@router.post("/", response_model=BookingResponse)
def book_ticket(
    booking: BookingCreate,
    db: Session = Depends(get_db)
):
    try:
        return booking_service.book_ticket(db, booking)

    except ValueError as e:
        status_code = 404 if str(e) == "Bus not found" else 400
        raise HTTPException(status_code=status_code, detail=str(e))


# GET ALL BOOKINGS
@router.get("/", response_model=list[BookingResponse])
def get_all_bookings(db: Session = Depends(get_db)):
    return booking_service.get_all_bookings(db)


# GET BOOKING BY ID
@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = booking_service.get_booking_by_id(db, booking_id)

    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")

    return booking


# CANCEL BOOKING
@router.delete("/{booking_id}")
def cancel_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):
    try:
        booking = booking_service.cancel_booking(db, booking_id)

        return {
            "message": "Ticket cancelled successfully",
            "booking_id": booking.id,
            "status": booking.status
        }

    except ValueError as e:
        status_code = 404 if str(e) in [
            "Booking not found",
            "Associated bus not found"
        ] else 400

        raise HTTPException(status_code=status_code, detail=str(e))