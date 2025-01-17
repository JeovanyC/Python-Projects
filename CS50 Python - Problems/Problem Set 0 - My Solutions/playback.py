def getSloow(sentence):
    return sentence.replace(" ", "...")

phrase = str(input("> "))
print(getSloow(phrase))