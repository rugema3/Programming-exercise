#!/usr/bin/python3

class Employees:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


    @property
    def age_limit(self):
        return self.age

    @age_limit.setter
    def age_limit(self, age):
        if age < 18:
            print("You are not allowed to apply")
        elif age > 65:
            print("You are retired.")
        else:
            print("You are welcome to Remmittance LLC.")

first = Employees('Alex', 22, 45000)
first.age_limit = 22
print()
first.age_limit = 90

