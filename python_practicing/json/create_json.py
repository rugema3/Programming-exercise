import json

# Create a dictionary representing a person
person = {
    "name": "Alice",
    "age": 25,
    "city": "San Francisco",
    "is_student": True,
    "hobbies": ["painting", "traveling", "yoga"]
}

# Convert the dictionary to JSON data
json_data = json.dumps(person)
# Print the JSON data
print(json_data)

# Your code here

