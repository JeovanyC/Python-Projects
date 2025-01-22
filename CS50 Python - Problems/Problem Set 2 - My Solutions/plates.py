import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False
    
    for char in s:
        if char in string.punctuation or char in string.whitespace or char in string.ascii_lowercase:
            return False
        
    if not s[0:2].isalpha():
        return False
    
    fistDigitIndex = next((i for i, char in enumerate(s) if char.isdigit()), -1)

    if fistDigitIndex != -1:
        if s[fistDigitIndex] == "0":
            return False
    
        if not s[fistDigitIndex].isdigit():
            return False
        
    return True


main()