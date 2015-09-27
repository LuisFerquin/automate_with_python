spam = ['apples', 'cats', 'bananas', 'tofu', 'apples', 'cats']

def listIntoString(aList):
    for i in range(len(aList)):
        if i == 0:
            print(aList[i].capitalize() + ', ', end="")
        elif i == len(aList)-1:
            print('and ' + aList[i] + '.')
        else:
            print(aList[i] + ', ', end="")


listIntoString(spam)