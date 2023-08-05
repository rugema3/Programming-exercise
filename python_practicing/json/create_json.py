#!/usr/bin/env python3
"""Define create_json module."""
import json

class Myjson():
    """Define Myjson class for JSON serialization and deserialization."""
    def __init__(self, filename):
        """Initialize Myjson instance with a filename."""
        self.filename = filename

    def save_to_json(self, data):
        """Save data to the JSON file."""
        with open(self.filename, 'a') as f:
            json.dump(data, f)
            f.write('\n')  # Add a newline to separate entries

    def load_from_json(self):
        """Load JSON data from the file and return as Python object."""
        try:
            with open(self.filename, 'r') as json_file:
                data = json.load(json_file)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            return None

def main():
    filename = "data.json"  # Use a fixed filename
    my_json = Myjson(filename)

    while True:
        print("\nPlease choose what you want to do: ")
        print("'1' for displaying the contents of the file.")
        print("'2' for adding contents to the file.")
        print("'3' to exit.")
        choice = input("Please enter your choice: ")

        if choice == '1':
            data = my_json.load_from_json()
            if data is not None:
                print(data)
            else:
                print("Error: Unable to read JSON file.")

        elif choice == '2':
            try:
                name = input("Please enter the name: ")
                age = input("Please enter the age: ")
                city = input("Please enter the city: ")
                
                data = my_json.load_from_json() or []  # Load existing data or create a new list
                entry = {
                    "name": name,
                    "age": age,
                    "city": city
                    # Add more fields as needed
                }
                data.append(entry)
                
                my_json.save_to_json(data)
                print("Data added and saved successfully.")
            except json.JSONDecodeError:
                print("Error: Invalid JSON data.")

        elif choice == '3':
            break

        else:
            print("Please choose a valid option.")

if __name__ == '__main__':
    main()

