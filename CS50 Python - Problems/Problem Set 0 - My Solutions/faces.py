def getEmoticon(string):
    string = string.replace(":)", "🙂").replace(":(", "🙁")
    print(string)

print("*Say something*")
phrase = str(input("> "))

getEmoticon(phrase)