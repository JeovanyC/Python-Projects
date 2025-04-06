from table_manipulator import path_table as pt
import fonts

def run_table() -> None:

    currenty = choice_path_1t()

    font = fonts.valid_fonts()

    while True:

        fonts.print_table(currenty, font)

        choice_list_2 = pt.get_choice_table_2()
        currenty = pt.table_path_2(choice_list_2, currenty)

def choice_path_1t() -> list:

    while True:

        choice_list_1 = pt.get_choice_table_1()
        currenty = pt.table_path_1(choice_list_1)

        if not currenty:

            print("The list is empty. Please, try again")
            continue

        return currenty