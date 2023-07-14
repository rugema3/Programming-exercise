#!/usr/bin/python3
"""employee_class Nodule."""


class Employees:
    """Define Employee Class."""

    def __init__(self, name, age, salary):
        """Define init method.

        Args:
        name: The name of the employee.
        age: The age of the employee.
        salary: The salary of the employee.
        """
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

    @property
    def payment(self):
        return self.salary

    @payment.setter
    def payment(self, salary):
        if self.salary > 10000:
            return f"You have more than 5 years under your belt"
        else:
            print("You have less than 5 years experience.")


first = Employees('Alex', 22, 45000)
second = Employees('Rugema', 34, 9)
first.age_limit = 22
print()
first.age_limit = 90
print()
second.payment = 87000

