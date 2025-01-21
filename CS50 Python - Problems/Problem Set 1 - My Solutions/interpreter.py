def getResult(operation):
    x, y, z = operation.split(" ")

    x = float(x)
    z = float(z)

    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "x" or y == "*":
        print(x * z)
    elif y == "/":
        if z != 0:
         print(x / z)
        else:
            print("Division by 0 is not possible")
    else:
        print("Invalid expression")

expression = input("Expression (ex: 3 + 1): ")

getResult(expression)