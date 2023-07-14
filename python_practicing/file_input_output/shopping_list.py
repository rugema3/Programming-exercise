#!/usr/bin/python3
"""Shopping_list Module."""


def create_list(filename, item):
    """Add an item to the shopping list file."""
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(item + "\n")
    except Exception as e:
        print("An error occurred while trying to write to the file:", str(e))

def read_list(filename):
    """Read and return the contents of the shopping list file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print("An error occurred while trying to read the file:", str(e))

if __name__ == '__main__':
    filename = 'shopping_list.txt'
    item = input("Please enter an item for your shopping list: ")
    finish = 'done'
    while item.lower() != finish:
        if item.lower() == 'clear':
            with open(filename, 'w', encoding='utf-8') as file:
                file.write("")
            print("The shopping list has been cleared.")
            break
        else:
            create_list(filename, item)
            item = input("Please enter another item for your shopping list or enter 'done' to quit: ")

    print("Thank you for creating your shopping list.")
    print("Here is your list of items to shop:\n")
    print(read_list(filename))
    


