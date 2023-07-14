#!/usr/bin/python3
"""create_file module."""

def create_file(filename, text):
    """Define the create_file method.

    Description:
    This function will create a file named "filename"
    and write "text" into it.

    Args:
    filename: the name of the file to be created.
    text: The text to be inserted into the file or the contents.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def read_file(filename):
    """Define read_file function.

    Description:
    This function reads the contents of a file.
   
    Args:
    filename: The name of the file
    """

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
        

if __name__ == "__main__":
    create_file('my_file.txt', 'Hello, world')
    read_file('my_file.txt')

