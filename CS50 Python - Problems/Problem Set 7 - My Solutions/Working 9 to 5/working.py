import re

def main() -> None:
    hours = input("Hours: ")

    earlyMid, afterMid = convert(hours)

    print(f"{earlyMid} to {afterMid}")


def convert(hours: str) -> tuple:
    hours = hours.strip()

    hoursPattern = r"(\d{1,2})(?::(\d{2}))? ?(AM|PM) (\d{1,2})(?::(\d{2}))? ?(AM|PM)"
    matchs = re.fullmatch(hoursPattern, hours)

    if not matchs:
        raise ValueError
    
    h1, min1, period1, h2, min2, period2 = matchs.groups()

    h1, h2 = int(h1), int(h2)
    min1 = int(min1) if min1 else 0
    min2 = int(min2) if min2 else 0

    if not (1 <= h1 <= 12 and 0 <= min1 < 60 and 1 <= h2 <= 12 and 0 <= min2 < 60):
        raise ValueError

    h1 = convert24(h1, period1)
    h2 = convert24(h2, period2)

    earlyMid = f"{h1:02}:{min1:02}"
    afterMid = f"{h2:02}:{min2:02}"

    return earlyMid, afterMid


def convert24(hour: int, period: str) -> int:
    if period == "AM":
        return 0 if hour == 12 else hour
    else:
        return hour if hour == 12 else hour + 12


if __name__ == "__main__":
    main()