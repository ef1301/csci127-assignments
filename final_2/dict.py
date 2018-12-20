def addline(d,line):
    lower = line.lower()
    split = lower.split()
    for item in split:
        l = []
        print(item)
        if item[0] in d:
            d[item[0]].append(item)
            d[item[0]].append(l)
        else:
            l.append(item)
            d.setdefault(item[0],l)
    return d
print(addline({},"Cats Birds donkey Dove"))
