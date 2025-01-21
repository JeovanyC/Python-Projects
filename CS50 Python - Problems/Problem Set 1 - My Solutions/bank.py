def getPromise(greatings):
    if greatings.lower().startswith("hello"):
        print("$0")
    elif greatings.lower().startswith("h"):
        print("$20")
    else:
        print("$100")
        
compliment = input("> ")

getPromise(compliment)