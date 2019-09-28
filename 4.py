def thirdHighest(text):
    x = []
    y = 0
    if type(text) != type(x):
        print("Parameter should be an array!")
    if len(text) < 3:
        print("Minimal array length is 3!")
    # for i in text:
    #     if type(i) == type(y) :
    #         x = i
    print(text[3])
                
thirdHighest([1,'b',3,5,4])