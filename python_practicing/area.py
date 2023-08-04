#!/usr/bin/python3

def area(height, width):
    if height <= 0 or width  <= 0:
        raise ValueError("both height and width must be > 0")
    else:
        return height * width

