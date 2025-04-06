import sys

def main() -> None:
    print('''
Hello!

Welcome to my binary/decimal number manipulator.''')
    try:
        while True:
            print('''
What you want to do?

  1. Convert a decimal number to binary
  2. Convert a binary number to decimal

(Q or Ctrl + Z to exit)''')
            while True:
                choice = input("> ")

                if choice in ["1", "2", "Q"]:
                    break

                print("Sorry... you can't do that...")

            if choice.upper() == "Q":
                print("Well, ok then!")
                sys.exit()

            if choice == "1":
                future_binary = get_number()

                print(f"{future_binary} in binary is {bin(future_binary)}")
                continue

            if choice == "2":
                future_decimal = get_binary()

                print(f"{future_decimal} in decimal is {int(future_decimal, 2)}")
                continue

    except EOFError:
        print("Well, ok then!")
        sys.exit()

def get_number() -> int:
    print("What number do you want to convert?")
    while True:
        number = input("> ")

        if number.isdecimal():
            number = int(number)
            return number

        print("Sorry... that is not a number...")

def get_binary() -> str:
    print("What number do you want to convert?")
    while True:
        binary_number = input("> ")

        if all(i in ["0", "1"] for i in binary_number):
            return binary_number

        print("Sorry... that is not a binary number")


if __name__ == "__main__":
    main()