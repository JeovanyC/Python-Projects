from PIL import Image, ImageOps
import sys

def main():
    inputFile, outputFile  =  getArguments()

    

    if not inputFile.strip():
        sys.exit("Missing a input")
    if not outputFile.strip():
        sys.exit("Missing a output")
    
    validFormats = (".jpg", ".jpeg", ".png")

    if not inputFile.lower().endswith(validFormats):
        sys.exit("Invalid input")
    if not outputFile.lower().endswith(validFormats):
        sys.exit("Invalid output")

    if inputFile.split(".")[-1].lower() != outputFile.split(".")[-1].lower():
        sys.exit("Input and output have different extensions")

    try:
        image = Image.open(inputFile)

    except FileNotFoundError:
        sys.exit("File does not exist")
    except Exception as e:
        sys.exit(f"Error found when opening the file: {e}")

    try:
        shirt = Image.open("shirt.png")

    except FileNotFoundError:
        sys.exit("File does not exist")
    except Exception as e:
        sys.exit(f"Error found when opening the file: {e}")

    image = ImageOps.fit(image, shirt.size)

    image.paste(shirt, mask=shirt)
    
    image.save(outputFile)
    print(f"Success! Saved as {outputFile}")


def getArguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    return sys.argv[1], sys.argv[2]


if __name__ == "__main__":
    main()