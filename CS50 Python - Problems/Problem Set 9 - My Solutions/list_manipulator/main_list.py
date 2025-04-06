from list_manipulator import path_list as pl
import fonts

def run_list() -> None:

    currenty = choice_path_1l()

    font = fonts.valid_fonts()

    while True:

        fonts.print_list(currenty, font)

        choice_list_2 = pl.get_choice_list_2()
        currenty = pl.list_path_2(choice_list_2, currenty)

def choice_path_1l() -> list:

    while True:

        choice_list_1 = pl.get_choice_list_1()
        currenty = pl.list_path_1(choice_list_1)

        if not currenty:

            print("The list is empty. Please, try again")
            continue

        return currenty