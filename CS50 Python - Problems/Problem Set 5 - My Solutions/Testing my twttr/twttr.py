def main():
    phrase = input("Input: ")
    sortedPhrase = shorten(phrase)

    print(sortedPhrase)

def shorten(word):
    vowels = "aeiou"

    for i in word:
        if i in vowels:
            word = word.replace(i, "")
    
    return word


if __name__ == "__main__":
    main()