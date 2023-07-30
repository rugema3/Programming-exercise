"""
Define animal module.

Description:
    This module will define the animal class with
    attributes name, species, age and sound.

    It will also define different methods such as
    make_sound(): This will produce the characteristic sound of an animal.
    description(): A method that prints a description of the animal,
                   including its name, species, and age.
    birthday():  The method that will return the birthday of an animal.
"""

import datetime


class Animal():
    """Define Animal class."""

    def __init__(self, name, species, age, sound):
        """
        Define the init method.

        attributes:
        name(str):      The name of the animal
        species(str):   The species an animal belongs.
        age(int):       The age of an animal.
        sound(str):     The sound the animal makes.
        """
        self.name = name
        self.species = species
        if not isinstance(age, int): # check if age is an integer
            raise TypeError("Age must be an integer")
        else:
            self.age = age

        self.sound = sound

    def make_sound(self):
        """Define make_sound method.

        This method returns the sound produced by the animal.
        """
        return f"The sound is {self.sound}"
    def description(self):
        """Define description method.

        This method tells the details of an animal.
        """
        return f"The {self.name} is {self.age} years old, makes {self.sound} sound and belongs to {self.species} species."

    def birthday(self):
        """Define birthday method.

        This returns the name of the animal and it's birthday.
        """
        current_year = datetime.datetime.now().year # obtain the current year
        dob = current_year - self.age

        return f"The {self.name} was born in {dob}"

    def __str__(self):
        """Define the string representation of the Animal instance."""

        return f"{self.name} (Species: {self.species}, Age: {self.age}, Sound: {self.sound})"
