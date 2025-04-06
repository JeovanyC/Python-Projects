from list_manipulator import main_list as ml
from table_manipulator import main_table as mt
import sys

def main() -> None:

    entry_choice = get_entry_choice()
            
    if entry_choice == "Q":

        print("Well, ok then!")
        sys.exit()

    if entry_choice == "1":

        ml.run_list()

    if entry_choice == "2":

        mt.run_table()

def get_entry_choice() -> str:

    print('''
Hi!
          
Welcome to this list/table manipulator!

What do you want to do?
                  
  1. Manipulate/create a list
  2. Manipulate/create a table
                  
(Q to exit)''')

    while True:

        choice = input("> ").strip().upper()

        print()

        if not choice in ["1", "2", "Q"]:
            
            print("That is not a available choice. Please, try again")
            continue

        return choice


if __name__ == "__main__":
    main()