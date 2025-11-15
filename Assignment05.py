# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using conditional logic and looping
# Change Log: (Who, When, What)
#   Rroot, 1/1/2030, Created Script
#   Ed Buchmayer, 11/14/2025, Updated Script
# ------------------------------------------------------------------------------------------ #

import json
import _io

# Define the Data Constants
MENU: str = """

---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-------------------------------------
"""

# Define the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
student_data: dict = {}  # One row of student data
students: list = []  # A table of student data
file_data: str = ''  # Holds combined string data separated by a comma.
file = _io.TextIOWrapper  # This is the actual type of the file handler
message: str = ''  # Holds a custom message string
FILE_NAME: str = 'Enrollments.json'

# Read the json file and load the data into the students list
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

    # Present the menu of choices
while True:
    print(MENU)
    choice = input("Enter a menu option: ")

    match choice:
        # Input user data
        case "1":
            try:
                # Input the data
                student_first_name = input("What is the student's first name? ")
                if not student_first_name.isalpha():
                    raise ValueError("The first name should not contain numbers.")
                student_last_name = input("What is the student's last name? ")
                if not student_last_name.isalpha():
                    raise ValueError("The last name should not contain numbers.")
                course_name = input("What is the course name? ")
                student_data = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
                students.append(student_data)
            except ValueError as e:
                print(e)  # Prints the custom message
                print("-- Technical Error Message -- ")
                print(e.__doc__)
                print(e.__str__())
            except Exception as e:
                print("There was a non-specific error!\n")
                print("-- Technical Error Message -- ")
                print(e, e.__doc__, type(e), sep='\n')
            continue
        # Present the current data
        case "2":
            message = " {} {} is registered for {}."
            for student in students:
                print(f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}')
            continue
        # Save the data to a file
        case "3":
            try:
                file = open(FILE_NAME, "w")
                json.dump(students, file, indent=2)  # Adding the indent option to format the JSON file.
                file.close()
                print("\nThe following list of dictionaries has been saved to Enrollments.json:")
                print(students)
                print("\nData written to Enrollments.json in a more readable format:")
                message = " {} {} is registered for {}."
                for student in students:
                    print(f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}')
                continue
            except TypeError as e:
                print("Please check that the data is a valid JSON format\n")
                print("-- Technical Error Message -- ")
                print(e, e.__doc__, type(e), sep='\n')
            except Exception as e:
                print("-- Technical Error Message -- ")
                print("Built-In Python error info: ")
                print(e, e.__doc__, type(e), sep='\n')
            finally:
                if file.closed == False:
                    file.close()
        # Stop the loop
        case "4":
            break
        case other:
            print("Invalid Entry")
            continue
