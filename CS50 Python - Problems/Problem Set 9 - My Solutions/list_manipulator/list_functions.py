def get_new_list() -> list:

    print("How many lines do you want? (10 max)")

    while True:

        num_lines = input("> ").strip()

        if not num_lines.isdigit():

            print("That is not a number. Please, try again")
            continue

        num_lines = int(num_lines)

        if not (1 <= num_lines <= 10):
            
            print("That is out of our range. Please, try 1-10 lines")
            continue

        break
    
    new_list = [item for _ in range(num_lines) for item in "x"]

    return new_list

def read_txt_l(file: str) -> list:

    with open(file, "r") as txt_file:
        lines = txt_file.readlines()

    loaded_file = [line.strip() for line in lines]

    print("File as been load sucessefuly!")

    return loaded_file

def get_line(any_list: list) -> int:

    print("Please, enter a index line number")

    while True:

        line_number = input("> ").strip()

        if not line_number.isdigit():

            print("That is not a index number. Please, try again")
            continue
        
        line_number = int(line_number)

        if not (1 <= line_number <= len(any_list)):
            
            print("That index number does not exist. Please, try again")
            continue

        break
    
    return line_number - 1

def get_mark() -> str:

    print("*Type your marker*")

    while True:

        marker =  input("> ").strip()

        if not marker:
            print("That is not a marker...")

            continue

        break

    return marker