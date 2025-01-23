import emoji

def main():
    phrase = input("Input: ")
    emojiPhase =  emoji.emojize(phrase, language="alias")

    print(f"Output: {emojiPhase}" )

if __name__ == "__main__":
    main()
