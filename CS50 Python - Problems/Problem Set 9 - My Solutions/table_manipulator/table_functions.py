import utils

def get_new_table() -> list:

    print("How many columns do you want?")
    column_wanted = utils.get_number()

    print()

    print("How many rows do you want?")
    rows_wanted = utils.get_number() 

    table = [["x" for _ in range(column_wanted)] for _ in range(rows_wanted)]

    return table

def read_txt_t(file: str) -> list:

    with open(file, "r") as txt_file:
        lines = txt_file.readlines()

    loaded_file = [line.strip().split(", ") for line in lines]

    return loaded_file

def get_column(any_table: list) -> int:

    print("Please, enter a index column number")

    while True:

        column_number = utils.get_number()
        
        column_number = int(column_number)
        if not (1  <= column_number <= len(any_table[0])):

            print("That is not a valid index number. Please, try again")
            continue

        break
        
    return column_number - 1

def get_row(any_table: list) -> int:

    print("Please, enter a index row number")
    
    while True:

        row_number = utils.get_number()

        row_number = int(row_number)

        if not (1  <= row_number <= len(any_table)):

            print("That is not a valid index number. Please, try again")
            continue

        break
    
    return row_number - 1