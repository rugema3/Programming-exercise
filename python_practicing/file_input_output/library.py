#!/usr/bin/python3
import os


def update_lib(filename, dict_name):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write("\n" + str(dict_name))


def read_content(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def search_book(title, filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    if title in content:
        book_lines = content.split('---\n')  # Split the content into book sections
        for book in book_lines:
            if title in book:
                book_details = book.strip().split('\n')
                print("The requested book is available. Here are the details of the book:\n")
                for detail in book_details:
                    attribute_value = detail.split(': ')
                    if len(attribute_value) == 2:
                        attribute, value = attribute_value
                        print(f"{attribute}: {value}")
                break
    else:
        print("The book is not available in our library.")


def del_book(title, filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.readlines()

    updated_content = []
    found_book = False
    for line in content:
        if f"Title: {title}" not in line:
            updated_content.append(line)
        else:
            found_book = True

    if found_book:
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(updated_content)
        print("The book has been successfully deleted.")
    else:
        print("The book was not found in the library.")


def create_file(filename):
    if not os.path.isfile(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            pass  # Create an empty file


if __name__ == '__main__':
    filename = 'library_inventory.txt'
    create_file(filename)  # Create the file if it doesn't exist

    title = input("Please enter the book title: ")
    author = input("Please enter the author: ")
    year = input("Please enter the publication year: ")
    ISBN = input("Please enter the ISBN: ")

    my_dict = {'title': title, 'author': author, 'year': year, 'ISBN': ISBN}
    update_lib(filename, my_dict)  # Append the book details to the file

    while True:
        user_input = input("Do you want to add more books? (yes/no): ")
        if user_input.lower() == "no":
            print("Thank you for adding the books.\n")
            break  # Exit the loop if the user chooses not to add more books
        elif user_input.lower() == "yes":
            title = input("Please enter the book title: ")
            author = input("Please enter the author: ")
            year = input("Please enter the publication year: ")
            ISBN = input("Please enter the ISBN: ")
            my_dict = {'title': title, 'author': author, 'year': year, 'ISBN': ISBN}
            update_lib(filename, my_dict)  # Append the book details to the file
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    print("The library has the following books with their details: \n")
    print(read_content(filename))
    print("\n")

    title = input("Please enter the book you are looking for: ")
    search_book(title, filename)

    title = input("Please enter the book you want to delete: ")
    del_book(title, filename)

