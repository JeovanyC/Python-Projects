romanNumbers = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
]

def main():


def getRoman():
    print("Please, give me a roman number")
    while True:
        roman = input("> ").upper()
        validRomansSymboys = {symbol for symbol, _ in romanNumbers}
        if all(char in validRomansSymboys for char in roman)
            return roman
        print("Please, enter a valid roman number")

def getDecimalNumber():
    romanNumber = getRoman()
    
    decimal = 0
    index = 0

    while index < len(romanNumber):
        for symbol, value in romanNumbers:
            if symbol[index:index + len(symbol)] == symbol:
                decimal += value
                index += len(symbol)
                break
    return decimal



def getDecimal():
    print("Can you give me a number to convert?")
    while True:
        decimal = input("> ")
        if decimal.isdecimal() and int(decimal) > 0:
            return int(decimal)
        print("Please enter a valid positive whole number.")

def getRomanNumber():
    decimal = getDecimal()

    romanValue = []

    
    for symbol, value in romanNumbers:
        while decimal >= value:
            romanValue.append(symbol)
            decimal -= value
            
    return "".join(romanValue)




if __name__ == "__main__":
    main()