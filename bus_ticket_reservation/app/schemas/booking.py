from pydantic import BaseModel, ConfigDict, Field


class BookingCreate(BaseModel):
    passenger_name: str
    phone: str
    bus_id: int
    seats_booked: int = Field(gt=0)


class BookingResponse(BaseModel):
    id: int
    passenger_name: str
    phone: str
    bus_id: int
    seats_booked: int
    status: str

    model_config = ConfigDict(from_attributes=True)