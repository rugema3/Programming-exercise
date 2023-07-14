#!/usr/bin/python3
"""library_catalog module.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Description:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module defines a class Book with attributes title, author,
publication year, available. This module will let the management know 
if the book is available for borrowing or not.
"""
class Book:
    """Define the Book class."""

    def __init__(self, title, author, year, available):
       
       """Initialize a book.

       Args:

       title(str): The title of the book.
       author(str): The author of the book.
       year(int): The publication year of the book.
       available(boolean): check whether the book is available or not.
       
       """
       self.title = title
       self.author = author
       self.year = year
       self.available = available

    def borrow(self):
        """
        This method will let the user borrow the book
        and set the available value to False.
        """
        self.available = False
        return self.available

    def bring_back(self):
        """
        This method will set the availability 
        of the book to True since it will be returned
        and ready to borrowed.
        """
        self.available = True
        return self.available


book1 = Book('Phyisics for Today and Tommorrow', 'Tom Duncan', 1998, True)
print(book1.borrow())
print()
print(book1.borrow())
print(book1.bring_back())







                            
