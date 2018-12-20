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

def spellcheck(d,word):
    lower = word.lower()
    if lower[0] in d:
        if lower in d[lower[0]]:
            return True
        else:
            return False
    return False
d = addline({},"Cats Birds donkey Dove")
print(spellcheck(d,"donkey"))
print(spellcheck(d,"cats"))
print(spellcheck(d,"Bird"))
print(spellcheck(d,"Birds"))