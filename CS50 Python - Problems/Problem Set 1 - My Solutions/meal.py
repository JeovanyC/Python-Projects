def main():
    hours = convert()

    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

def convert():
    time = input("What time is it? ")
    hours, minutes = time.split(":")

    hours = float(hours)
    minutes = float(minutes)

    hours = (minutes / 60) + hours

    return hours
if __name__ == "__main__":
    main()