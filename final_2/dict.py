def addline(d,line):
    lower = line.lower()
    split = lower.split()
    for item in split:
        l = []
        print(item)
        if item[0] in d:
            l.append(item)
            d[item[0]] = l
        else:
            d.setdefault(item[0],0)
            l.append(item)
            d[item[0]] = l
    return d
print(addline({},"Cats Birds donkey dove"))