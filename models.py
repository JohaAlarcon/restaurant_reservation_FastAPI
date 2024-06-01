from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Reservation(Base):

  __tablename__ = "reservations"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  date = Column(DateTime)
  num_people = Column(Integer)
