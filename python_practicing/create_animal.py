from animal import Animal

# Global list to store animals in the zoo
zoo = []

def create_animal():
    """Define create_animal.

    Description:
        This function creates an animal dynamically.
    """
    while True:
        name = input("Please enter the name of the animal or stop to quit: ")
        if name.lower() == 'stop':
            print("You are stopping animal entry. See you next time.")
            break
        
        species = input("Please enter the Species of the animal: ")
        age = int(input("Please enter the age of the animal: "))
        sound = input("What sound does it make? ")
        animal_instance = Animal(name, species, age, sound)
        zoo.append(animal_instance)
        print(animal_instance.description())
        print()
        print(animal_instance.birthday())
        print()

def show_zoo():
    """Define show_zoo.

    Description:    This function shows the list of 
                    animals in teh zoo.

    """
    if len(zoo) == 0:
        print("There have no animals in the zoo.")
    else:
        print("Animals in the zoo: ")
        for animal in zoo:
            print(animal)

if __name__ == '__main__':
    """Main function to handle user choices."""
    while True:
        print("\nWhat would you like to do?")
        print("1. Create an animal")
        print("2. View animals in the zoo")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            create_animal()
        elif choice == '2':
            show_zoo()

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
