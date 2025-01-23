def main():
    months =  [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    
    while True:
        date = input("Date: ").strip()

        if any(month.lower() in date.lower() for month in months):
            try:
                month, day, year = date.split(" ")
                
                month = month.capitalize()
                if month in months:
                    month = months.index(month) + 1
                
                day = int(day.replace(",", ""))
                month = int(month)
                year = int(year)

                if 1 <= day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                else:
                    print("Invalid date: day out of range.")

            except (ValueError, IndexError):
                print("Invalid date: incorrect format.")

        elif "/" in date:
            try:
                month, day, year = date.split("/")

                day = int(day)
                month = int(month)
                year = int(year)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                else:
                    print("Invalid date: month or day out of range.")
                
            except (ValueError, IndexError):
                print("Invalid date: incorrect format.")

        else:
            print("Invalid date: unsupported format.")


if __name__ == "__main__":
    main()