import main as return_function
import sys, os

def close_program() -> None:

    print("Well, ok then!")
    sys.exit()

def menu_return() -> None:

    print("Ok than! Returning to main menu...")
    return_function.main()

def load_file() -> None:

    print("Ok than! Can you please give me a .txt file?")

    while True:

        file = input("> ").strip()

        if not file.endswith(".txt"):

            file += ".txt"

        if not os.path.exists(file):

            print("We are not able to find your file. Please, try again")
            print()

            continue

        return file

def get_change() -> str:

    print("*Type your change*")

    while True:

        change =  input("> ").strip()

        if not change:

            print("That is not a change. Please, try again")
            continue

        break

    return change

def get_number() -> int:

    while True:

        number = input("> ").strip()

        try:

            return int(number)
        
        except ValueError:

            print("That is not a number. Please, try again")

def get_name() -> None:

    print("How do you like to name your file?")

    while True:

        name = input("> ").strip()

        if name[0].isdecimal():

            print("Your name can not start with a number character. Please, try again")
            continue

        break

    if not name.endswith(".txt"):
        name += ".txt"
        
    return name