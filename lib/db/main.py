import sys
import sqlite3
from cars import Car
from maintenance import Maintenance
from comments import Comment

db_path = '/home/lenny/development/Phase-3/Project/Drivers-Drive/lib/db/car_management.db'


def create_tables():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create cars table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            vin TEXT PRIMARY KEY,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    ''')

    # Create maintenance table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS maintenance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_vin TEXT NOT NULL,
            maintenance_type TEXT NOT NULL,
            description TEXT,
            date_performed TEXT NOT NULL,
            FOREIGN KEY (car_vin) REFERENCES cars(vin) ON DELETE CASCADE
        )
    ''')

    # Create comments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            maintenance_id INTEGER NOT NULL,
            comment_text TEXT NOT NULL,
            FOREIGN KEY (maintenance_id) REFERENCES maintenance(id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()

def list_cars():
    cars = Car.get_all()
    for car in cars:
        print(car)

def find_car_by_make():
    make = input("Enter the car's make: ")
    cars = Car.find_by_make(make)
    for car in cars:
        print(car) if car else print(f'Car with make {make} not found')

def find_car_by_vin():
    vin = input("Enter the car's VIN: ")
    car = Car.find_by_id(vin)
    if car:
        print(car)
    else:
        print(f'Car with VIN {vin} not found')

def create_car():
    vin = input("Enter the car's VIN: ")
    make = input("Enter the car's make: ")
    model = input("Enter the car's model: ")
    year = int(input("Enter the car's year: "))

    try:
        car = Car(vin, make, model, year)
        car.save()
        print(f'Successfully created car: {car}')
    except Exception as exc:
        print("Error creating car:", exc)

def update_car():
    vin = input("Enter the car's VIN: ")
    car = Car.find_by_id(vin)
    if car:
        make = input("Enter the car's new make: ")
        model = input("Enter the car's new model: ")
        year = int(input("Enter the car's new year: "))
        car.make = make
        car.model = model
        car.year = year
        car.save()
        print(f'Successfully updated car: {car}')
    else:
        print(f'Car with VIN {vin} not found')

def delete_car():
    vin = input("Enter the car's VIN: ")
    car = Car.find_by_id(vin)
    if car:
        car.delete()
        print(f'Successfully deleted car: {car}')
    else:
        print(f'Car with VIN {vin} not found')

def list_maintenances():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM maintenance")
        maintenances = cursor.fetchall()

        for maintenance in maintenances:
            print(maintenance)

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    finally:
        conn.close()

def find_maintenance_by_id():
    id_ = input("Enter the maintenance's id: ")
    maintenance = Maintenance.find_by_id(id_)
    print(maintenance) if maintenance else print(f'Maintenance with id {id_} not found')

def create_maintenance():
    car_vin = input("Enter the car's VIN: ")
    maintenance_type = input("Enter the maintenance type: ")
    description = input("Enter the maintenance description: ")
    date_performed = input("Enter the date performed: ")
    try:
        maintenance = Maintenance(None, car_vin, maintenance_type, description, date_performed)
        maintenance.save()
        print(f'Success: {maintenance}')
    except Exception as exc:
        print("Error creating maintenance:", exc)

def update_maintenance():
    id_ = input("Enter the maintenance's id: ")
    maintenance = Maintenance.find_by_id(id_)
    if maintenance:
        car_vin = input("Enter the car's VIN: ")
        maintenance_type = input("Enter the maintenance type: ")
        description = input("Enter the maintenance description: ")
        date_performed = input("Enter the date performed: ")
        try:
            maintenance.car_vin = car_vin
            maintenance.maintenance_type = maintenance_type
            maintenance.description = description
            maintenance.date_performed = date_performed
            maintenance.save()
            print(f'Successfully updated maintenance: {maintenance}')
        except Exception as exc:
            print("Error updating maintenance:", exc)
    else:
        print(f'Maintenance with ID {id_} not found')

def delete_maintenance():
    id_ = input("Enter the maintenance's id: ")
    maintenance = Maintenance.find_by_id(id_)
    if maintenance:
        maintenance.delete()
        print(f'Successfully deleted maintenance: {maintenance}')
    else:
        print(f'Maintenance with ID {id_} not found')


def list_comments():
    comments = Comment.get_all()
    for comment in comments:
        print(comment)

def find_comment_by_id():
    id_ = input("Enter the comment's id: ")
    comment = Comment.find_by_id(id_)
    print(comment) if comment else print(f'Comment with id {id_} not found')


def create_comment():
    maintenance_id = input("Enter the maintenance's id: ")
    comment_text = input("Enter the comment: ")
    try:
        comment = Comment(None, maintenance_id, comment_text)
        comment.save()
        print(f'Success: Comment {comment.id} created')
    except Exception as exc:
        print("Error creating comment:", exc)

def update_comment():
    id_ = input("Enter the comment's id: ")
    comment = Comment.find_by_id(id_)
    if comment:
        new_comment_text = input("Enter the comment's new text: ")
        comment.update(new_comment=new_comment_text)
        print(f'Success: Updated comment with id {id_}')
    else:
        print(f'Comment with id {id_} not found')

def delete_comment():
    id_ = input("Enter the comment's id: ")
    comment = Comment.find_by_id(id_)
    if comment:
        comment.delete()
        print(f'Comment {id_} deleted')
    else:
        print(f'Comment with id {id_} not found')

def print_menu(title, options):
    print("\n" + "=" * 40)
    print(f"{title:^40}")
    print("=" * 40)
    for key, value in options.items():
        print(f"{key}. {value}")
    print("=" * 40)

def main():
    main_menu_options = {
        "0": "Exit the program",
        "1": "Cars Menu",
        "2": "Maintenance Menu",
        "3": "Comments Menu"
    }

    car_menu_options = {
        "0": "Back to Main Menu",
        "1": "List all cars",
        "2": "Find car by make",
        "3": "Find car by VIN",
        "4": "Create car",
        "5": "Update car",
        "6": "Delete car"
    }

    maintenance_menu_options = {
        "0": "Back to Main Menu",
        "1": "List all maintenances",
        "2": "Find maintenance by id",
        "3": "Create maintenance",
        "4": "Update maintenance",
        "5": "Delete maintenance"
    }

    comment_menu_options = {
        "0": "Back to Main Menu",
        "1": "List all comments",
        "2": "Find comment by id",
        "3": "Create comment",
        "4": "Update comment",
        "5": "Delete comment"
    }

    while True:
        print_menu("MAIN MENU", main_menu_options)
        choice = input("> ")

        if choice == "0":
            print("Goodbye!")
            sys.exit()
        elif choice == "1":
            while True:
                print_menu("CARS MENU", car_menu_options)
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
        elif choice == "2":
            while True:
                print_menu("MAINTENANCE MENU", maintenance_menu_options)
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    list_maintenances()
                elif choice == "2":
                    find_maintenance_by_id()
                elif choice == "3":
                    create_maintenance()
                elif choice == "4":
                    update_maintenance()
                elif choice == "5":
                    delete_maintenance()
                else:
                    print("Invalid choice! Please enter a valid option.")
        elif choice == "3":
            while True:
                print_menu("COMMENTS MENU", comment_menu_options)
                choice = input("> ")
                if choice == "0":
                    break
                elif choice == "1":
                    list_comments()
                elif choice == "2":
                    find_comment_by_id()
                elif choice == "3":
                    create_comment()
                elif choice == "4":
                    update_comment()
                elif choice == "5":
                    delete_comment()
                else:
                    print("Invalid choice! Please enter a valid option.")
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    create_tables()  
    main()  
