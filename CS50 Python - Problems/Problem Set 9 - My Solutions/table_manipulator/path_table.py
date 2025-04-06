from table_manipulator import custom_table as ct
from table_manipulator import table_functions as tf
import utils

def get_choice_table_1() -> str:

    print('''
What you want to do?

  1. Create a new table
  2. Load a previous table
  3. Return to main page
                  
(Q to exit)''')

    while True:
            
        choice = input("> ").upper()

        print()

        if not choice in ["1", "2", "3", "Q"]:
        
            print("That is not a available choice. Please, try again")
            continue

        return choice
    
def table_path_1(entry: str) -> list:

    match entry:

        case "Q":
        
            utils.close_program()

        case "3":
        
            utils.menu_return()

        case "1":

            table_modifiable = tf.get_new_table()
            return table_modifiable

        case "2":

            file = utils.load_file()
            table_modifiable = tf.read_txt_t(file)

            return table_modifiable
            
def get_choice_table_2() -> str:

    print('''
What you want to do now?

  1. Modify a cell
  2. Add one or more columns
  3. Add one or more rows
  4. Clear a cell
  5. Clear all cells
  6. Remove a column
  7. Remove a row
  8. Save the file and exit
  9. Return to main page
                  
(Q to exit)''')

    while True:

        choice = input("> ").upper()

        print()

        if not choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Q"]:

            print("That is not a available choice. Please, try again")
            continue

        return choice
    
def table_path_2(entry: str, currenty: list) -> list:

    match entry:

        case "Q":
            utils.close_program()
        
        case "9":
            utils.menu_return()

    table_modifiable = ct.CustomTable(currenty)

    match entry:

        case "8":

            name = utils.get_name()
            print()

            table_modifiable.save_table(name)

        case "1":

            column = tf.get_column(table_modifiable)
            print()

            row = tf.get_row(table_modifiable)
            print()

            change = utils.get_change()

            table_modifiable.modify_cell(column, row, change)
            return table_modifiable

        case "2":

            print("How many columns do you want to add?")
            number = utils.get_number()

            table_modifiable.add_column(number)
            return table_modifiable
        
        case "3":

            print("How many rows do you want to add?")
            number = utils.get_number()

            table_modifiable.add_row(number)
            return table_modifiable

        case "4":

            column = tf.get_column(table_modifiable)
            print()

            row = tf.get_row(table_modifiable)
            print()

            table_modifiable.clear_cell(column, row)
            return table_modifiable

        case "5":

            table_modifiable.clear_cells()
            return table_modifiable
        
        case "6":

            column = tf.get_column(table_modifiable)

            table_modifiable.remove_column(column)
            return table_modifiable

        case "7":

            row = tf.get_row(table_modifiable)

            table_modifiable.remove_row(row)
            return table_modifiable