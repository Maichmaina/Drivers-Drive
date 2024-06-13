# cli.py

import sys
from cars import Base, Car
from maintenance import Maintenance
from comments import Comment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database connection URL
DB_URL = 'sqlite:///car_rental.db'

# Create the SQLAlchemy engine
engine = create_engine(DB_URL)

# Bind the engine to the Base class
Base.metadata.bind = engine

# Create all tables in the database (if they don't exist)
Base.metadata.create_all(engine)

# Create a session maker bound to the engine
Session = sessionmaker(bind=engine)

# Define other functions and main menu code...

def list_cars():
    session = Session()
    cars = session.query(Car).all()
    for car in cars:
        print(car)

def find_car_by_make():
    session = Session()
    make = input("Enter the car's make: ")
    cars = session.query(Car).filter(Car.make == make).all()
    for car in cars:
        print(car) if car else print(f'Car with make {make} not found')

def find_car_by_vin():
    session = Session()
    vin = input("Enter the car's VIN: ")
    car = session.query(Car).filter(Car.vin == vin).first()
    if car:
        print(car)
    else:
        print(f'Car with VIN {vin} not found')

# Define other functions...

def main():
    # Main menu options...

    while True:
        # Display main menu...

        choice = input("> ")

        if choice == "0":
            print("Goodbye!")
            sys.exit()
        elif choice == "1":
            # Cars menu
            while True:
                # Display cars menu...

                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    list_cars()
                elif choice == "2":
                    find_car_by_make()
                elif choice == "3":
                    find_car_by_vin()
                elif choice == "4":
                    create_car()
                elif choice == "5":
                    update_car()
                elif choice == "6":
                    delete_car()
                else:
                    print("Invalid choice! Please enter a valid option.")
       

if __name__ == "__main__":
    main()
