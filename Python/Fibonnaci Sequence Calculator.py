def main():
    fibonnaciN = getUntil()
    counter = 0

    a = 0
    b = 1
    while counter <= fibonnaciN:
        i = a + b
        a = b
        b = i
        print(a)
        counter += 1


def getUntil():
    print(
'''Hi

This is Fibonnaci Number calculator. If you want to calculate,
in a more simple way, n Fibonnaci numbers, you have come to the
right place!

How many numbers you want to know?
''')
    
    while True:
        until = input("> ")
        if until.isdecimal() and int(until) > 0:
            return (int(until) - 1)
        
        print("Please, try a whole postive number.")
        continue


if __name__ == "__main__":
    main()