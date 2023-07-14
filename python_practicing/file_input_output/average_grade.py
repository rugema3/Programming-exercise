#!/usr/bin/python3
"""Average_grade module.
Description:

This module handles the creation of a file named "grades.txt"
and writes a list of grades each on a seperate line.

It contains another method that handles the reading of the contents
of a file.
"""

def write_grades(filename, grades):
    """Define write_grade function.
    
    Decription:
                This function writes the contents
                in a file. the contents in this case are
                the grades of the students.
                Each content/grade is written on a seperate line.
    Args:

    filename:   the name of the file.
    grades:     The grades/contents to be written in a file.

    """

    with open(filename, 'a',encoding='utf-8') as file:
        file.write(str(grades) +"\n")


def read_grades(filename):
    """Define the read_grades function.

    Description:
                    This function reads the contents of a file.
    Args:
    filename:   The name of the file.
    Return:     The grades in the file.

    """
    with open(filename, 'r' ,encoding='utf-8') as file:
        grades = file.read()
    return grades

def average_grade(filename):
    """Define average_grade function.

    Description:    This function computes the average of 
                    grades as read from the file.Because
                    each grade is written in a seperate line,
                    we use the splitlines() method which takes 
                    care of the \n.
                    Note that we converted the grades from string to int.

    Args:

    filename:       The name of the file.
    Return:         The average of the grades.
    """
    count = 0
    total = 0
    with open(filename, 'r' ,encoding='utf-8') as file_read:
        my_file = file_read.read()
        grades = my_file.splitlines() #
        for grade in grades:
            total = total + int(grade)
            count = count + 1
    return total / count

if __name__ == '__main__':
    grades = [85, 92, 78, 90, 88, 30]
    for grade in grades:
        write_grades('grades.txt', grade)
        
    print(read_grades('grades.txt'))
    print()
    print('The average is: {}'.format(average_grade('grades.txt')))
