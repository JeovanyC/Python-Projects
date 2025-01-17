import random

numberLenght = 3
maxGuesses = 10


def main():
    print(
f'''I'm trying to remember a number, but I not sure what it's...
Can you help me? I have some clues to help you:

 1. I'm looking for a ditinsh {numberLenght} digit number;
 2. If I, for some reason say "Fermi", "Pico" or "Bagels"; here what it means:

    a. "Fermi"  ---> One digit correct and in the right position;
    b. "Pico"   ---> One digit correct but in the wrong positon;
    c. "Bagels" ---> No digits are correct.

Thanks for your help! I really apreciate.
''')
    while True:
        number = getNumber()
        numGuess = 1
        print(f"To be more of a challenge, you have a total of {maxGuesses} guesses to make")
        print()
        while numGuess <= maxGuesses:
            guess = ""
            while len(guess) != numberLenght or not guess.isdecimal():
                print ("Guess {}: ".format(numGuess))
                guess = input("> ")
            
            hints = clues(guess, number)
            print(hints)
            print()
            numGuess += 1

            if guess == number:
                print("But... I'm not sure...")
                break

            if numGuess > maxGuesses:
                print(f"You ran out of guesses. Beside this, don't worry, you can try again!")
                print("The answer taht you ha looking for is {number}")
        print("Are you willing to help me again? (yes or no)" + "\n")
        if not input("> ").lower().startswith("y"):
            break
    print()
    print("Thanks fo playing")


def getNumber():
    n = list("0123456789")
    random.shuffle(n)
    number = []

    for i in range(numberLenght):
        number += str(n[i])
    return "".join(number)


def clues(guess, number):

    if guess == number:
        return "That it! You found out!"

    hints = []

    for i in range(len(guess)):
        if guess[i] == number[i]:
            hints.append("Fermi")
        elif guess[i] in number:
            hints.append("Pico")

    if len(hints) == 0:
        return "Bagels"
    
    else:
        hints.sort()
        return " ".join(hints)
    
        

if __name__ == "__main__":
    main()
