import json

data = 'numbers.json'
# Read data from the input JSON file
with open(data, 'r', encoding='utf-8') as file:
    data_loaded = json.load(file)

print(data_loaded)
values_list = []
for value in data_loaded.values():
    values_list.append(value)
print(values_list)

# The file "input.json" contains JSON data representing a list of numbers
# Read the data, double each number, and store the result in a new list

# Write the modified list to a new JSON file called "output.json"

# Your code here

