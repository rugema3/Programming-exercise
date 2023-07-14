#!/usr/bin/python3

import math

"""
circle_operations module.

Description:
=====================================================================

This module will calculate the area and 
the circumfrence of a circle.

"""

class Circle:
    """Define the circle class."""

    pi_value = math.pi

    def __init__(self, radius):
        """Initiolization of a circle attributes.

        Args:

        r: The radius of a circle.
        """

        self.radius = radius
        if not isinstance(self.radius, (int,float)):
            raise TypeError("The radius must be an int or float.")
        if radius < 0:
            raise ValueError("the radius must be a positive integer.")


    def get_area(self):
        
        """
        This method calculates the area of 
        a circle given its radius.
        """

        return self.pi_value * (self.radius ** 2)

    def get_circumfrence(self):
        
        """
        This method calculated the circumfrence
        of a circle given its radius.
        """

        return 2 * self.pi_value * self.radius


circle1 = Circle(7)
print("The area of a circle is: {:.02f})".format(circle1.get_area()))
print()
print("The circumference of a circle is: {:.02f}".format(circle1.get_circumfrence()))



