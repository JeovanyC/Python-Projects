from pyfiglet import Figlet
import sys

def main():
    typeFont = getFont()

    try:
        phrase =  input("Input: ")

        if not phrase.strip():
            print("Error: Phrase cannot be empty")
            sys.exit(1)

        chooseFont = Figlet(font=typeFont)
        drawPhrase =  chooseFont.renderText(phrase)

        print(drawPhrase)

    except (ValueError, IndexError):
        print("Invalid font")
        sys.exit(1)

def getFont():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        return "standard"
    
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
        if sys.argv[2] in fonts:
            return sys.argv[2]
        
        else:
            print("Invalid usage")
            sys.exit(1)
    else:
        raise ValueError("Invalid prompt arguments")


if __name__ == "__main__":
    main()