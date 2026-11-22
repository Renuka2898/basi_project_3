from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.connection import Base


class Booking(Base):

    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    passenger_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    bus_id = Column(Integer, ForeignKey("buses.id"))
    seats_booked = Column(Integer, nullable=False)
    status = Column(String, default="confirmed")