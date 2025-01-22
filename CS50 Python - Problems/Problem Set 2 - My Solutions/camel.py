def getSnakeCase(camelCase):
    snakeCase = ""

    for i in camelCase:
        if i.isupper():
            snakeCase += "_" + i.lower()
        else:
            snakeCase += i
    
    print(snakeCase)

namePhrase = input("camelCase: ")

getSnakeCase(namePhrase)