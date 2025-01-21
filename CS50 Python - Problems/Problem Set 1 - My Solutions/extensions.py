fileExtensions = {
    ".gif": "image",
    ".jpg": "image",
    ".jpeg": "image",
    ".png": "image",
    ".pdf": "application",
    ".txt": "text",
    ".zip": "application"
}

def getFileExtension(file):
    for fileName, fileType in fileExtensions.items():
        if file.endswith(fileName):
            print(fileType, fileName.replace(".", ""), sep="/")
            return
    print("application/octet-stream")

print("What file you want to know about?")
fileGiven = input("> ")

getFileExtension(fileGiven)