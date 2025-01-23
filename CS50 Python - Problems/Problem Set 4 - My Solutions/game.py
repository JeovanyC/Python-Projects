import random

def main():
    level = getRange()

    number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))

            if guess == number:
                print("Just right!")
                break

            elif guess > number:
                print("Too large!")
            else:
                print("Too small!")

        except ValueError:
            print("Input a positive integer")

def getRange():
    while True:
        try:
            range = int(input("Level: "))

            if range > 0:
                return range
            
            print("Input a positive integer")

        except ValueError:
            print("Enter a valid integer")

if __name__ == "__main__":
    main()