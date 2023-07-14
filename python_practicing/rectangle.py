#!/usr/bin/python3
"""rectangle Module."""

class Rectangle:
    """Define the Rectangle class."""

    def __init__(self, length=0, width=0):
        """Define init method.

        Args:
            length: The length of the rectangle.
            width: The width of the rectangle.
        """
        try:
            self.length = int(length)
            self.width = int(width)
        except ValueError:
            raise TypeError("The length and width must be integers.")

        if self.length < 0 or self.width < 0:
            raise ValueError("The length and width must be non-negative values.")

    @property
    def area(self):
        return self.width * self.length

# Create the instance of the Rectangle class
rectangle1 = Rectangle(10, 20)
print("The area of a rectangle with a width of {} and length of {} is: {}".format(rectangle1.width, rectangle1.length, rectangle1.area))

try:
    rectangle2 = Rectangle(-20, 5)
    print(rectangle2.area)
except ValueError as e:
    print("Error:", str(e))

