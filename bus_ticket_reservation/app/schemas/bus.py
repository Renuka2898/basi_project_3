from pydantic import BaseModel, ConfigDict, Field
from datetime import date


class BusCreate(BaseModel):
    bus_name: str
    source: str
    destination: str
    travel_date: date
    total_seats: int = Field(gt=0)
    price: float = Field(gt=0)


class BusResponse(BaseModel):
    id: int
    bus_name: str
    source: str
    destination: str
    travel_date: date
    total_seats: int
    available_seats: int
    price: float

    model_config = ConfigDict(from_attributes=True)