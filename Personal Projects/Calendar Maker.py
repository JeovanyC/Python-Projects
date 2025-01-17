import datetime


days = ("Sunday","Monday", "Tuesday", "Wednesday",
        "Thuesday", "Friday", "Saturnday")

months = ("January", "Febuary", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December" )


print(
'''Want to see the calendar in a more "stalish way"?
You come to the right place!
''')

while True:
    print('''
Please in what year you a looking for?
''')
    response =  input("> ")

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    else:
        print("Please, a numeric year as 2024")
        continue


while True:
    print('''
In what numeric month? (like: 10 --> October )
''')
    response_m = input("> ")

    if not response_m.isdecimal():
        print('''
What?... can you try again?...
''')
        continue
    
    month = int(response_m)
    if 1 <= month <= 12:
        break

    print("Try a month between 1 - 12")

def getCalendar(year, month):
    calText = ""

    calText += (" " * 34) + months[month - 1] + " " + str(year) + "\n"
    calText += "   Sunday     Monday    Tuesday    Wednesday  Thursday    Friday    Saturday  \n"

    weekSeparator = ("+----------" * 7) + "+\n"

    blankRow = ('|          ' * 7) + '|\n'

    currentDate = datetime.date(year, month, 1)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days = 1)
    
    while True:
        calText += weekSeparator

        dayNumberRow = ""
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += "|" + dayNumberLabel + (" " * 8)
            currentDate += datetime.timedelta(days = 1)
        dayNumberRow += "|\n"

        calText += dayNumberRow
        for i in range(3):
            calText += blankRow
            
        if currentDate.month != month:
            break
    
    calText += weekSeparator
    return calText

calText = getCalendar(year, month)
print(calText)


print('''
Here are the calendar you asked. You are Welcome!
''')