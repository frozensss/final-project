## What I Learned

In this final project, I learned how to combine many of the Python programming skills from the course into one complete application. The Dog Rescue program uses a menu that allows the user to add a dog, view all dogs, search for a dog by name, or quit the program.

I learned how to organize a larger program by using functions. Instead of writing all of the code in one section, I used separate functions for `main()`, `menu()`, `addDog()`, `viewDogs()`, and `findDog()`. This made the program easier to read, test, and update.

I also practiced using a `while` loop for the menu. The loop keeps the program running until the user selects the quit option. Inside the loop, I used `if`, `elif`, and `else` statements to decide which function should run based on the user's menu choice.

Another important skill I practiced was storing related data in a list. Each dog is stored as a dictionary with a name, breed, age, and weight. The dictionaries are stored inside one list called `dogs`. This helped me understand how lists and dictionaries can work together to store multiple records.

I learned how to use a `for` loop to process data in a list. The `viewDogs()` function loops through the list and displays each dog in columns. The `findDog()` function also uses a loop to search through the list and check whether the dog name entered by the user matches one of the stored dogs.

I also practiced input validation with `try` and `except`. The program checks that the age and weight entered by the user are valid numbers before saving the dog record. This helps prevent the program from crashing if the user types the wrong kind of input.
