import random

def main():
    level = getLevel()

    levelCount = 0
    score = 0

    while levelCount < 10:
        errorCounter = 0

        a = generateInteger(level)
        b = generateInteger(level)

        correctAnswer = a + b

        while errorCounter < 3:
            try:
                answer = int(input(f"{a} + {b} = "))

                if answer == correctAnswer:
                    levelCount += 1
                    score += 1
                    break

                else:
                    print("EEE")
                    errorCounter += 1
            except ValueError:
                print("EEE")
                errorCounter += 1

        if errorCounter == 3:
            print(f"{a} + {b} = {correctAnswer}")
            levelCount += 1
    
    print(f"Score: {score}")


def getLevel():
    while True:
        try:
            level = int(input("Level: "))

            if level == 1:
                numberRange = 10
                return numberRange
            
            if level == 2:
                numberRange = 100
                return numberRange
            
            if level == 3:
                numberRange = 1000
                return numberRange
            
            else:
                print("Invalid level")
        
        except ValueError:
            print("Invalid input")


def generateInteger(range):
    return random.randint(1, range)

if __name__ == "__main__":
    main()