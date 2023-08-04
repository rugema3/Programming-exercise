import json

# JSON data
json_data = '{"name": "John Doe", "age": 30, "city": "New York", "is_student": false, "hobbies": ["reading", "swimming", "coding"]}'

# Parse JSON data
data = json.loads(json_data)

# Access specific values
# 1. Print the name
print(data['name'])
# 2. Print the age
print(data['age'])
# 3. Print the city
print(data['city'])
# 4. Print whether the person is a student or not
print(data['is_student'])
# 5. Print the first hobby in the list
print(data['hobbies'][1])

# Your code here

