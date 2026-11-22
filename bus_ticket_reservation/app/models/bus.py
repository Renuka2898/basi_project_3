from sqlalchemy import Column, Integer, String, Date, Float
from app.database.connection import Base


class Bus(Base):

    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)
    bus_name = Column(String, nullable=False)
    source = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    travel_date = Column(Date, nullable=False)
    total_seats = Column(Integer, nullable=False)
    available_seats = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)