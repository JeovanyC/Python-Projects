numberList = [2, 7, 11, 15]   # You can alter this numbers as you want.
target = 17                   # Also, this target number can also be alter.

for i in numberList:
    for j in numberList:      # To have a combination of three numbers to a target is just need to:
        if i + j == target:   #   add another for "something" in numberList;
            print(i and j)    #   and add this "something" to the print to be outputed.