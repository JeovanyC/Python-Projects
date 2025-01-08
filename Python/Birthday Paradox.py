import datetime, random


def getBirthdays(number_Birthdays):

    birthdays = []

    for i in range(number_Birthdays):
        start_Y = datetime.date(2001, 1, 1)

        random_D = datetime.timedelta(random.randint(0, 364))

        birthday = start_Y + random_D
        birthdays.append(birthday)
    return birthdays


def birthday_M(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a +1 :]):
            if birthdayA == birthdayB:
                return birthdayA


print(
'''It's sed that in a group a people is a high change of two individuals
having the same birthday.

This is a interest curiosity that is called "Birthday Paradox".
Let's do a little test to see this so named "paradox".
''')


months = ("Jan.", "Feb.", "Mar.", "Apr.", "May.", "Jun.",
          "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec.")


while True:
    print("How many hypothetical birthdays should we generate for our test? (Max 100)" + "\n")
    answer =  input("> ")
    if answer.isdecimal() or (0 < int(answer) <= 100):
        number_B = int(answer)
        break

print("\n" +"Here are the {} birthdays for our test:".format(number_B) + "\n")
birthdays = getBirthdays(number_B)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(", ", end = "")
    month_N = months[birthday.month - 1]
    dateText = "{} {}".format(month_N, birthday.day)
    print(dateText, end = "")


match =  birthday_M(birthdays)

print()
print("\n" + "In this simulation", end = "")
if match != None:
    month_N = months[match.month - 1]
    dateText = "{} {}".format(month_N, match.day)
    print("\n" + "There are one or more people with matching birthdays.")
else:
    print("\n" + "There are no matching birthdays.")

print()
print("Generating", number_B, "random birthdays 100,000 times...")
input("Press Enter to begin...")

print("\n" + "Let's run another 100,000 simulations.")
print()
simMatch = 0

for i in range(100_000):
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birthdays = getBirthdays(number_B)
    if birthday_M(birthdays) != None:
        simMatch += 1
print()

print("100,000 simulations run.")
print()


probability = round(simMatch / 100_000 * 100, 2)
print(
'''Out of 100,000 simulations of {} people, there was a matching birthday 
in that group {} times. This means that {} people have a {} % chance of
having a matching birthday in their group.

That's probably more than you would think!
'''.format(number_B, simMatch, number_B, probability ))