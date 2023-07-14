#!/usr/bin/python3
"""Numbers_operations module."""


def number_ops(filename, nums):
    """Number_ops function.

    Args:

    filename: name of the file.
    nums: the range of numbers.
    """
    with open(filename, 'w' ,encoding='utf-8') as file:
        my_list = [str(i) for i in range(0, nums+1)]
        for item in my_list:
            file.write(item + "\n")

def add_nums(filename):
    """Define add_nums functions.
    Description:
                This function will read the contents of a file
                and add them to return the sum of the numbers
                in the file.

    Args:

    filename:   the name of the file.
    Return:     The sum of the contents of a file.

    """
    with open(filename, 'r' ,encoding='utf-8') as file:
        total = 0
        num = file.readline()
        for num in file:
            num = int(num)
            print(num)
            total = num + total
    print(total)




if __name__ == "__main__":
    number_ops('numbers.txt', 20)
    add_nums('numbers.txt')
