#!/usr/bin/python3
"""
Student module.

This module provides a StudentDatabase class for managing student information.
"""

class StudentDatabase:
    """
    A class representing a student database.

    Methods:
    - __init__: Initialize an instance of StudentDatabase.
    - add_student: Add a student to the database.
    - retrieve_student: Retrieve a student from the database based on the name.
    - save_to_file: Save the database to a file.
    - load_from_file: Load the database from a file.
    """

    filename = 'students.txt'

    def __init__(self):
        """Initialize an instance of StudentDatabase."""
        self.students = []

    def add_student(self):
        """
        Add a student to the database.

        Prompts the user to enter the name, age, home town, and gender of the student
        and adds the student to the database.
        """
        name = input("Enter the name of the student: ")
        age = input("Enter the age of the student: ")
        home_town = input("Enter the home town: ")
        gender = input("Enter the gender of the student: ")
        student = {"name": name, "age": age, "home_town": home_town, "gender": gender}
        self.students.append(student)
        print("Student added.")

    def retrieve_student(self):
        """
        Retrieve a student from the database based on the name.

        Prompts the user to enter the name of the student to retrieve.
        If a student with the given name is found in the database,
        their details (name, age, home town, and gender) are displayed.
        If no student is found, a corresponding message is printed.
        """
        name = input("Enter the name of the student for retrieval: ")
        found_students = []
        for student in self.students:
            if student["name"] == name:
                found_students.append(student)
        if found_students:
            for student in found_students:
                print(f"Name: {student['name']}, Age: {student['age']}, Home: {student['home_town']}, Gender: {student['gender']}")
        else:
            print("No student found with that name.")

    def save_to_file(self):
        """
        Save the database to a file.

        Writes the details of all students in the database to a file.
        Each student's details are written on a separate line in the format:
        name, age, home town, gender
        """
        with open(self.filename, 'a', encoding='utf-8') as file:
            for student in self.students:
                file.write(f"{student['name']}, {student['age']}, {student['home_town']}, {student['gender']}\n")
        print("Database saved to the file.")

    def load_from_file(self):
        """
        Load the database from a file.

        Reads the details of students from a file and populates the database.
        Each line in the file represents a student with the format:
        name, age, home town, gender
        """
        self.students = []
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    name, age, home_town, gender = line.split(",")
                    student = {"name": name, "age": age, "home_town": home_town, "gender": gender}
                    self.students.append(student)
        print("Database loaded from the file.")
        print(self.students)


def main():
    """
    Run the main program loop.

    Displays a menu of options to the user and performs the corresponding actions
    based on their input until the user chooses to quit.
    """
    student_db = StudentDatabase()

    while True:
        print("Student Database")
        print("1. Add student")
        print("2. Retrieve student")
        print("3. Save database")
        print("4. Load database")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_db.add_student()

        elif choice == '2':
            student_db.retrieve_student()

        elif choice == '3':
            student_db.save_to_file()

        elif choice == '4':
            student_db.load_from_file()

        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()

