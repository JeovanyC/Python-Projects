from list_manipulator import custom_list as cl
from list_manipulator import list_functions as lf
import utils

def get_choice_list_1() -> str:

    print('''
What you want to do?

  1. Create a new list
  2. Load a previous list
  3. Return to main page
                  
(Q to exit)''')
    
    while True:

        choice = input("> ").strip().upper()

        print()

        if not choice in ["1", "2", "3", "Q"]:

            print("That is not a available choice. Please, try again")
            continue

        return choice
    
def list_path_1(entry: str) -> list:

    match entry:
    
        case "Q":
    
            utils.close_program()

        case "3":
    
            utils.menu_return()

        case "1":

            list_modifiable = lf.get_new_list()
            return list_modifiable

        case "2":

            file = utils.load_file()
            list_modifiable = lf.read_txt_l(file)

            return list_modifiable

def get_choice_list_2() -> str:

    print('''
What you want to do now?

  1. Modify a line
  2. Add one or more lines
  3. Clear a line
  4. Clear all lines
  5. Remove a line
  6. Mark a line as done                
  7. Save the file and exit
  8. Return to main page
                  
(Q to exit)''')
            
    while True:

        choice = input("> ").strip().upper()

        print()

        if not choice in ["1", "2", "3", "4", "5", "6", "7", "8", "Q"]:

            print("That is not a available choice. Please, try again")
            continue

        return choice

def list_path_2(entry: str, currenty: list) -> list:


    match entry:

        case "Q":

            utils.close_program()

        case "8":

            utils.menu_return()

    list_modifiable = cl.CustomList(currenty)

    match entry:

        case "7":

            name = utils.get_name()

            list_modifiable.save_list(name)

        case "1":

            line = lf.get_line(list_modifiable)

            print()

            change = utils.get_change()

            list_modifiable.modify_line(line, change)
            return list_modifiable

        case "2":

            print("How many lines do you want to add?")
            number = utils.get_number()

            list_modifiable.add_lines(number)
            return list_modifiable

        case "3":

            line = lf.get_line(list_modifiable)

            list_modifiable.clear_line(line)
            return list_modifiable

        case "4":

            list_modifiable.clear_lines()
            return list_modifiable

        case "5":

            line = lf.get_line(list_modifiable)

            list_modifiable.remove_line(line)
            return list_modifiable

        case "6":

            line = lf.get_line(list_modifiable)

            print()

            mark = lf.get_mark()

            list_modifiable.add_mark(line, mark)
            return list_modifiable