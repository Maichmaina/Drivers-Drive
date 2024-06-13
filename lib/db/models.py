# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine('sqlite:///car_rental.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class CarType(Base):
    __tablename__ = 'car_types'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    rate_per_day = Column(Integer)
    cars = relationship("Car", back_populates="car_type")

    @classmethod
    def create(cls, name, rate_per_day):
        session = SessionLocal()
        car_type = cls(name=name, rate_per_day=rate_per_day)
        session.add(car_type)
        session.commit()
        return car_type

    @classmethod
    def delete(cls, id):
        session = SessionLocal()
        car_type = session.query(cls).filter(cls.id == id).first()
        session.delete(car_type)
        session.commit()

    @classmethod
    def get_all(cls):
        session = SessionLocal()
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        session = SessionLocal()
        return session.query(cls).filter(cls.id == id).first()

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    car_type_id = Column(Integer, ForeignKey('car_types.id'))
    car_type = relationship("CarType", back_populates="cars")

    @classmethod
    def create(cls, car_type_id):
        session = SessionLocal()
        car = cls(car_type_id=car_type_id)
        session.add(car)
        session.commit()
        return car

    @classmethod
    def delete(cls, id):
        session = SessionLocal()
        car = session.query(cls).filter(cls.id == id).first()
        session.delete(car)
        session.commit()

    @classmethod
    def get_all(cls):
        session = SessionLocal()
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        session = SessionLocal()
        return session.query(cls).filter(cls.id == id).first()
