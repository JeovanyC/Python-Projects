import time


def main():
    print(
'''Hello!

I'm FizzBuzz, and I have always been intrigued by numbers being divisible 
by the same number. If you also find this curiosity interesting, 
you've come to the right place!
''')
    
    a = getNumberA()
    b = getNumberB()

    print("What range do you want to check?")
    period = int(input("> "))

    print('''
Keep in mind!

FizzBuzz ---> If both numbers that you chose can devide the same number
Fizz     ---> If only the fist number can devide that number
Buzz     ---> If only the second number can devide that number

Now! Here it goes!
''')
    time.sleep(2)

    fizzBuzzCounter = 0
    fizzCounter = 0
    buzzCounter = 0

    fizzBuzzList = []
    fizzList = []
    buzzList = []

    for i in range(1, period + 1):
        if i % a == 0 and i % b == 0:
            print("FizzBuzz")
            fizzBuzzCounter += 1
            fizzBuzzList.append(i)

        elif i % b == 0:
            print("Fizz")
            fizzCounter += 1
            fizzList.append(i)

        elif i % a == 0:
            print("Buzz")
            buzzCounter += 1
            buzzList.append(i)

        print(i)
    print()
    
    print(f'''
In conclusion...

We had a total of:

{fizzBuzzCounter} FizzBuzz's  
{fizzBuzzList}

{fizzCounter} Fizz's
{fizzList}
          
{buzzCounter} Buzz's      
{buzzList}
          
Preaty interesting!
''')

    

def getNumberA():
    print("Can you please give me two number?")
    print()
    while True:
        numberA = input("> ")
        if numberA.isdecimal() and int(numberA) > 0:
            return int(numberA)
        print("A whole positive number, please.")
        continue

def getNumberB():
    print("Please provide the second number.")
    print()
    while True:
        numberB = input("> ")
        if numberB.isdecimal() and int(numberB) > 0:
            return int(numberB)
        print("A whole positive number, please.")
        continue

if __name__ == "__main__":
    main()