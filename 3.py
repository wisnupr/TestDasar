import re

def sortNumber(string):
    
    x = re.findall("[0-9]", string)
    if (x):
        x.sort()
        print(x)
    else:
        print("No number found in parameter!")

sortNumber("wisnu14523")