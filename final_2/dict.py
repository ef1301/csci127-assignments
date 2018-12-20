def addline(d,line):
    lower = line.lower()
    split = lower.split()
    for item in split:
        l = []
##        print(item)
        if item[0] in d:
            d[item[0]].append(item)
        else:
            l.append(item)
            d.setdefault(item[0],l)
    return d
print(addline({},"Cats Birds donkey Dove"))

def main(d,line):
    i = 0
    while i < 5:
        addline(d,line)
        i += 1
    return d
print(main({},"Cats Birds donkey Dove"))

##def spellcheck(d,word):
##    