def main():
    compliment = input("> ")
    
    print(value(compliment))


def value(greeting):
    if greeting.lower().startswith("hello"):
        return "$100"
    elif greeting.lower().startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()