# CIS 106 Final Project
# Dog Rescue Application

# Global list used to store all dog records
# Each dog is stored as a dictionary with name, breed, age, and weight

dogs = []


def main():
    #Set up the dog rescue program and call the menu.
    menu()


def display_menu():
    #Display the Dog Rescue menu
    print("\nDog Rescue")
    print("----------")
    print("1. Add a Dog")
    print("2. View Dogs")
    print("3. Find Dog")
    print("4. Quit")


def menu():
   #Use a while loop and if statements to get user menu choices
    choice = ""

    while choice != "4":
        display_menu()
        choice = input("\nSelect a choice: ")

        if choice == "1":
            addDog()
        elif choice == "2":
            viewDogs()
        elif choice == "3":
            findDog()
        elif choice == "4":
            print("\nThank you for using the Dog Rescue application.")
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")


def addDog():
    #Ask the user for dog information and store it in the list
    print("\nAdd a Dog")
    print("---------")

    dog_name = input("Dog Name: ")
    dog_breed = input("Dog Breed: ")

    # check age input
    while True:
        try:
            dog_age = int(input("Age: "))
            break
        except ValueError:
            print("Please enter a whole number for age.")

    # check weight input
    while True:
        try:
            dog_weight = float(input("Weight: "))
            break
        except ValueError:
            print("Please enter a number for weight.")

    dog = {
        "name": dog_name,
        "breed": dog_breed,
        "age": dog_age,
        "weight": dog_weight
    }

    dogs.append(dog)
    print(f"\n{dog_name} has been added to the rescue list.")


def viewDogs():
    #Use a for loop to display all dogs in the list
    print("\nRescue Dogs")
    print("-----------")

    if len(dogs) == 0:
        print("No dogs have been entered yet.")
    else:
        print(f"{'Dog':<15}{'Breed':<30}{'Age':>5}{'Weight':>10}")
        print("-" * 60)

        for dog in dogs:
            print(f"{dog['name']:<15}{dog['breed']:<30}{dog['age']:>5}{dog['weight']:>10.1f}")


def findDog():
    #Use a for loop to search for a dog by name
    print("\nFind Dog")
    print("--------")

    search_name = input("Enter dog name to search: ")
    found = False

    for dog in dogs:
        if dog["name"].lower() == search_name.lower():
            print(f"\nFound {dog['name']}")
            print(f"Breed: {dog['breed']}")
            print(f"Age: {dog['age']}")
            print(f"Weight: {dog['weight']:.1f}")
            found = True
            break

    if not found:
        print(f"\nSorry, unable to find {search_name}")


# start program
if __name__ == "__main__":
    main()
