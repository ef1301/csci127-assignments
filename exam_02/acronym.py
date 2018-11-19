def makeacronym(w):
    ac = []
    lower = w.lower()
##    print(lower)
##    split = lower.split()
##    print(split)
    ac.append(lower[0])
    for i in range(0,len(lower)):
##        print(i)
        if lower[i] == " ":
            if lower[i+1] in "abcdefghijklmnopqrstuvwxyz":
                ac.append(lower[i+1])
##                print(ac)
        else:
            continue
    return "".join(ac)

print(makeacronym("Laugh out Loud"))
print(makeacronym("Read the ... fine manuel"))
print(makeacronym("Rolling on Floor Laughing"))
print(makeacronym("in my humble opinion"))
print(makeacronym("In my not so humble opinion"))