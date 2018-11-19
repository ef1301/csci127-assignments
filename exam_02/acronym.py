def makeacronym(w):
    ac = []
    lower = w.lower()
    print(lower)
##    split = lower.split()
##    print(split)
    ac.append(lower[0])
    for item in lower:
        print(item)
        if item == " ":
            ac.append(lower[lower.index(item)+1])
            print(ac)
        else:
            continue
    return "".join(ac)

print(makeacronym("Laugh out Loud"))
