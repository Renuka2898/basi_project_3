from fastapi import FastAPI

from app.database.connection import Base, engine
from app.models import bus, booking
from app.routers import bus as bus_router
from app.routers import booking as booking_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bus Ticket Reservation API",
    description="Simple Bus Ticket Booking System",
    version="1.0.0"
)

app.include_router(bus_router.router)
app.include_router(booking_router.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Bus Ticket Reservation API"
    }