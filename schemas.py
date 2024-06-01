from pydantic import BaseModel, Field
from datetime import datetime

class ReservationBase(BaseModel):
  name: str
  date: datetime
  num_people: int = Field(..., gt=0, description="El numero de personas debe ser mayor que 0")

class ReservationCreate(ReservationBase):
  pass

class Reservation(ReservationBase):
  id: int

  class Config:
    orm_mode = True