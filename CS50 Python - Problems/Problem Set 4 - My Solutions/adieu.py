import inflect

def main():
    names = getNames()

    p = inflect.engine()

    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    else:
        formattedNames =  p.join(names)
        print(f"Adieu, adieu, to {formattedNames}")

def getNames():
    nameList = []

    try:
        while True:
            name = input("Name: ")
            nameList.append(name)
    except EOFError:
        return nameList
    
    
if __name__ == "__main__":
    main()