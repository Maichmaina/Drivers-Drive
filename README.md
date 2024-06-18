# Phase 3 CLI Project Template

## Drivers Drive

# Description
Drivers Drive is a command-line application designed to manage cars, their maintenance records, and associated comments. The system allows users to perform CRUD (Create, Read, Update, Delete) operations on cars, maintenance records, and comments.

# Problem Statement
 Drivers Drive is an automotive enthusiast and aspiring entrepreneur, developing a comprehensive car management system to streamline the tracking and maintenance of vehicles. The system needs to allow users to manage cars, maintenance records, and comments associated with each maintenance task efficiently.

# Solution
 The Drivers Drive System is a command-line interface (CLI) application designed to  helps organize and track vehicles but also serves as a foundation for potential future enhancements and features.

## Features

# Car Management:
Add, update, view, and delete cars.
Attributes include VIN (Vehicle Identification Number), make, model, and year.

# Maintenance Tracking:
Record maintenance activities performed on each car.
Details include maintenance type, description, date performed, and associated car.

# Comment System:
Leave comments on each maintenance record.
Comments are linked to specific maintenance records.

## Setup
# Clone the Repository:
git clone <repository-url>
cd car-management-system 

# Install Dependencies:
This project uses Python 3 and requires the sqlite3 module.
Ensure Python 3 is installed
python --version
No additional pip packages required beyond Python standard library

# Database Initialization:
The database (car_management.db) is created and initialized automatically when running the application for the first time.
Tables (cars, maintenance, comments) are created with necessary schemas.


## Usage
Run the Application: #python main.py

This starts the application and presents the main menu.
Use numeric options to navigate through Cars, Maintenance, and Comments menus.

# Navigating Menus:
Each menu provides options to perform CRUD operations:
I. Cars Menu: List cars, find by make or VIN, create, update, delete cars.
II. Maintenance Menu: List maintenances, find by ID, create, update, delete maintenance records.
III. Comments Menu: List comments, find by ID, create, update, delete comments.

# Data Management:
Follow on-screen prompts to interact with the system.
Ensure to input correct VINs, maintenance IDs, and follow data validation prompts.

# Exiting the Application:
Use option 0 to exit the program gracefully.

# Troubleshooting
Ensure Python 3 is correctly installed and accessible from the command line.
If encountering issues with database connectivity or schema initialization, verify sqlite3 module installation and database path (car_management.db).


## License
This project is licensed under the MIT License. See the LICENSE file for details.

# Author
Lennis Maina
