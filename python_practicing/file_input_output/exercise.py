#!/usr/bin/python3

def open_file(filename, text):

    #with open(filename, 'w', encoding='utf-8') as file:
     #   file.write(text + "\n")

    with open(filename, 'a' ,encoding='utf-8') as file:
        file.write(text +"\n")
        

    with open(filename, 'r',encoding='utf-8') as file:
        content = file.read()
        print(content)

if __name__ == '__main__': 
    open_file('exercise.txt', 'I am done with ALX')
    open_file('exercise.txt', 'what do you want from me')
    open_file('exercise.txt', 'I will deal with you.')


