"""see_animal module.
I have made this module an executable by adding the shebang.
"""
#!/usr/bin/env python3

from animal import Animal # importing the animal class in this module.

a = Animal('lion', 'carnivorous', 10, 'roars')
print(a.name) # print the name of the animal.
print()

print(a.description()) # Display the animal description
a.name = "cow"
a.species = "Herbivorous"
print(a.description()) # update some attributes to see the changes.
print()

# Create a list of dictionaries with different animals and their attributes.
animal_data = [
        {
            'name': 'Buffalo',
            'species':'Herbivorous',
            'age' : 25,
            'sound': 'MOO'
            },
        {
            'name': 'cat',
            'species': 'carnivorous',
            'age': 3,
            'sound': 'myawu myawu'
            },
        {
            'name': 'pig',
            'species': 'omnivorous',
            'age': 2,
            'sound': 'oik oik'
            },
        {
            'name': 'snake',
            'species': 'reptile',
            'age': 120,
            'sound': 'hiss hiss hiss'
            }
        ]

for data in animal_data: # Iterate over the list
    b = Animal(data['name'], data['species'], data['age'], data['sound'])
    print("The {} has the following details: ".format(b.name))
    print("==================================================================================================")
    print(b.description())
    print(b.birthday())
    print("==================================================================================================")
    print() # print a new line everytime you end the loop.


