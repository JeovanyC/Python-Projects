import re

def main() -> None:
    print(count(input("Text: ")))


def count(phrase: str) -> int:
    ocorrencyList = re.findall(r"um", phrase)
    
    return len(ocorrencyList)

if __name__ == "__main__":
    main()