from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'

    vin = Column(String, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)

    def __init__(self, vin, make, model, year):
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Car: VIN={self.vin}, Make={self.make}, Model={self.model}, Year={self.year}"





