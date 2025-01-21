def getGreatQuestion(answer):
    if answer == "42" or answer.replace("-", " ").strip().lower() == "forty two":
        print("Yes")
    else:
        print("No")

print("What is the Answer to the Great Question of Life, the Universe, and Everything?")
response = input("> ")

getGreatQuestion(response)