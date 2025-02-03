import sys

def main():
    file = validFile()

    try:
        with open(file, "r") as data:
            numberOfLines =  0

            for line in data:
                if line.strip().startswith("#") or not line.strip():
                    continue
                else:
                    numberOfLines += 1

    except FileNotFoundError:
        sys.exit("File does not exist")
    except Exception as e:
        sys.exit(f"Error found when opening the file: {e}")
    
    print(numberOfLines)
 
def validFile():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    fileName = sys.argv[1]

    if not fileName.strip():
        sys.exit("Missing argument")

    if not fileName.endswith(".py"):
        sys.exit("Not a Python file")

    return fileName


if __name__ == "__main__":
    main()