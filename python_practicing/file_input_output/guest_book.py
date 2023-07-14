#!/usr/bin/python3
"""Guest_book module.

Description:
            This program will ask the user his name
            and add the name of the guest on a file.
"""

def write_guest_name(filename, guest):
    """Write the name of a guest to a file.

    Args:
        filename (str): Name of the file where the guest names are stored.
        guest (str): The name of the guest.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(guest + "\n")

def print_guest_book(filename):
    """Print the contents of the guest book file.

    Args:
        filename (str): Name of the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

if __name__ == '__main__':
    filename = 'guest_book.txt'
    guest = input("Please enter your name: ")

    while guest != 'q':
        write_guest_name(filename, guest)
        guest = input("Please enter your name or 'q' to quit: ")

    print("I am done registering all the guests")
    print("Guest Book Contents:")
    print_guest_book(filename)


  
