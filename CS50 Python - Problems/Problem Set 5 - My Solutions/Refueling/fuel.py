def main():
    howMuchFuel = getFuel()

    if howMuchFuel > 99:
        print("F")
    elif howMuchFuel < 1:
        print("E")
    else:
        print(howMuchFuel, sep="")

def getFuel():
    while True:
        fuel = input("Fraction (ex: 2 / 3): ")
        
        x, z = fuel.split("/")
        
        x = int(x)
        z = int(z)
        
        if z == 0:
            print("Invalid fraction")
        elif "/" in fuel:
            percent = (x / z) * 100
            return str(percent)
        else:
            print("Not a valid fraction")

        
if __name__ == "__main__":
    main()