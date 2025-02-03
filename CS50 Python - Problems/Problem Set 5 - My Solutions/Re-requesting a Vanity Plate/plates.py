import string

def main():
    plate = input("Plate: ")
    if isValid(plate):
        print("Valid")
    else:
        print("Invalid")


def isValid(s):

    if len(s) < 2:
        return False
    
    # for char in s:
    #     if char in string.punctuation or char in string.whitespace or char in string.ascii_lowercase:
    #         return False
        
    if not s[0:2].isalpha():
        return False
    
    fistDigitIndex = next((i for i, char in enumerate(s) if char.isdigit()), -1)

    if fistDigitIndex != -1:
        # if s[fistDigitIndex] == "0":
            # return False
    
        if not s[fistDigitIndex].isdigit():
            return False
        
    return True


if __name__ == "__main__":
    main()