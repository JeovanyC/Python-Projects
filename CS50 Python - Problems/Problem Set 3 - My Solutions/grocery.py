from collections import Counter

def main():
    listGroceries = []

    while True:
        try:
            getGroceries = input("")
            listGroceries.append(getGroceries)

        except EOFError:
            break
    
    listGroceries = [item.upper() for item in listGroceries]
    listGroceries.sort()
    
    counter = Counter(listGroceries)
    
    finalDisplay = set()

    for i in listGroceries:
        if i not in finalDisplay:
            print(f"{counter[i]} {i}")
            finalDisplay.add(i)



if __name__ == "__main__":
    main()