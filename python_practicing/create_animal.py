"""Define create_animal module."""

from animal import Animal

def create_animal():
    """Define create_animal.

    Description:
                This function creates an animal dynamically.
    """
    zoo = [] # A list of animal instances.
    while True:
        name = input("Please enter the name of the animal or stop to quit: ")
        if name.lower() == 'stop':
            print("You are stopping animal entry. See you next time.")
            break # quit the loop when stop is entered by the user.
        species = input("Please enter the Species of the animal: ")
        age = int(input("Please enter the age of the animal: "))
        sound = input("What sound does it make? ")
        animal_instance = Animal(name, species, age, sound)
        zoo.append(animal_instance)
        print(animal_instance.description())
        print()
        print(animal_instance.birthday())
        print()
        print("Animals in the zoo: ")
        for animal_instance in zoo:
            print(animal_instance)

if __name__ == '__main__':
    create_animal()

