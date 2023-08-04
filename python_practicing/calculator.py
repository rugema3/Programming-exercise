#!/usr/bin/python3

def add(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Please use numbers")
        elif num1 is None or num2 is None:
            raise TypeError("Format error")

def swap(num1, num2):
    num1, num2 = num2, num1
    return (num1, num2)

def sub(num1, num2):
    return num1 + num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    try:
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Please use numbers")
        return num1 / num2
    except ZeroDivisionError:
        if num2 == 0:
            raise ZeroDivisionError("dicision by zero not allowed.")

