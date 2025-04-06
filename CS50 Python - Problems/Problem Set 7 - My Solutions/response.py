import validators

def main() -> None:
    email = input("What's your email address? ").strip()

    if validators.email(email) == True:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()