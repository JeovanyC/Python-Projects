from tabulate import tabulate
import csv, sys
        
def main():
    csvFile = validFile()

    try:
        with open(csvFile, "r") as data:
            values = csv.DictReader(data)
            data = [row for row in values]

            if not data:
                sys.exit()
            
            print(tabulate(data, headers="keys", tablefmt="grid"))
    
    except FileNotFoundError:
        sys.exit("File does not exist")
    except Exception as e:
        sys.exit(f"Error found when opening the file: {e}")
    
def validFile():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    fileName = sys.argv[1]

    if not fileName.strip():
        sys.exit("Missing argument")

    if not fileName.endswith(".csv"):
        sys.exit("Not a CSV file")

    return fileName


if __name__ == "__main__":
    main()