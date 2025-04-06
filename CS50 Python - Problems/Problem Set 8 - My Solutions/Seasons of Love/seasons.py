from datetime import date, datetime
import inflect, sys

def main() -> None:
    birthDate = input("Date of Birth: ").strip()

    if verifiedDate(birthDate) != True:
        sys.exit("Invalid date format")
    
    birthDate = datetime.strptime(birthDate, "%Y-%m-%d")
    now = datetime.now()

    totalMin = int((now - birthDate).total_seconds() / 60)

    numberWords = writeConvertion(totalMin)

    print(numberWords.capitalize())

def verifiedDate(date: str) -> bool:
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True

    except ValueError:
        return False

def writeConvertion(min: int) -> str:
    p = inflect.engine()
    numberWords = p.number_to_words(min).replace(" and", "")
    return f"{numberWords} minutes"



if __name__ == "__main__":
    main()