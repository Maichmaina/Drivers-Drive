from models import CarType, Car

def display_car_types():
    car_types = CarType.get_all()
    print("Car Types:")
    for car_type in car_types:
        print(f"ID: {car_type.id}, Name: {car_type.name}, Rate Per Day: {car_type.rate_per_day}")

def create_car_type():
    name = input("Enter car type name: ")
    rate_per_day = int(input("Enter rate per day: "))
    CarType.create(name, rate_per_day)
    print("Car type created successfully.")

def delete_car_type():
    display_car_types()
    id = int(input("Enter ID of car type to delete: "))
    CarType.delete(id)
    print("Car type deleted successfully.")

def display_cars():
    cars = Car.get_all()
    print("Cars:")
    for car in cars:
        print(f"ID: {car.id}, Car Type ID: {car.car_type_id}")

def create_car():
    display_car_types()
    car_type_id = int(input("Enter ID of car type: "))
    Car.create(car_type_id)
    print("Car created successfully.")

def delete_car():
    display_cars()
    id = int(input("Enter ID of car to delete: "))
    Car.delete(id)
    print("Car deleted successfully.")

def main():
    while True:
        print("\n1. Display Car Types")
        print("2. Create Car Type")
        print("3. Delete Car Type")
        print("4. Display Cars")
        print("5. Create Car")
        print("6. Delete Car")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_car_types()
        elif choice == 2:
            create_car_type()
        elif choice == 3:
            delete_car_type()
        elif choice == 4:
            display_cars()
        elif choice == 5:
            create_car()
        elif choice == 6:
            delete_car()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

