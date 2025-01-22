def main():
    vowels = "aeiouAEIOU"
    words = input("Input: ")

    for i in words:
        if i in vowels:
            words = words.replace(i, "")

    print(words)


if __name__ == "__main__":
    main()