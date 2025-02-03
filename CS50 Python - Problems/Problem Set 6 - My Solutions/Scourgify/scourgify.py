import csv, sys

def main():
    inputFile, outputFile = validFile()
    
    try:
        with open(inputFile, "r") as inFile:
            reader = csv.DictReader(inFile)

            columnName = "name"
            columnHouse = "house"

            values = []

            for row in reader:
                lastName, fistName = row[columnName].split(",")
                lastName, fistName = lastName.strip(), fistName.strip()

                values.append({
                    "first" : fistName,
                    "last" : lastName,
                    "house" : row[columnHouse],
                })

        with open(outputFile, "w", newline="") as outFile:
            writer = csv.DictWriter(outFile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(values)

            



    except FileNotFoundError:
        sys.exit("One or more files does not exist")
    except Exception as e:
        sys.exit(f"Error found when opening the file: {e}") 

def validFile():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]

    if not inputFileName.strip():
        sys.exit("Invalid input")
    if not outputFileName.strip():
        sys.exit("Invalid output")

    if not inputFileName.endswith(".csv"):
        sys.exit(f"Could not read {inputFileName}")
    if not outputFileName.endswith(".csv"):
        sys.exit(f"Could not read {outputFileName}")

    return inputFileName, outputFileName


if __name__ == "__main__":
    main()