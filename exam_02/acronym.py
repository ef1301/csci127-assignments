def makeacronym(w):
    ac = []
    lower = w.lower()
    print(lower)
    split = lower.split()
    print(split)
    for i in lower:
        ac.append(lower[0])
    return "".join(ac)

print(makeacronym("Laugh out Loud"))