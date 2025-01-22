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
                
                if month in months:
                    month = months.index(month) + 1

                day.replace(",", "")

                print(f"{year.zfill(4)}-{month.zfill(2)}-{day.zfill(2)}")

            except ValueError:
                print("Invalid date.")

        elif "/" in date:
            try:
                month, day, year = date.split("/")

                month =  int(month)
                day = int(day)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year.zfill(4)}-{month.zfill(2)}-{day.zfill(2)}")
                else:
                    print("Invalid date.")
                
            except ValueError:
                print("Invalid date.")

        else:
            print("Invalid date.")


if __name__ == "__main__":
    main()