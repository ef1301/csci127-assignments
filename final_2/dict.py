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
print(addline({},"Cats Birds donkey Dove camel coffee"))

##def main(d,line):
##    i = 0
##    while i < 5:
##        addline(d,line)
##        i += 1
##    return d
d = addline({},"Cats Birds donkey Dove camel coffee")
addline(d,"I don't know what I am doing")
addline(d,"Random words here")
addline(d,"Insert sad faces here")
addline(d,"May I please pass")
addline(d,"I guess not")
print(d)
##print(main({},"Cats Birds donkey Dove camel coffee"))

def spellcheck(d,word):
    lower = word.lower()
    if lower[0] in d:
        if lower in d[lower[0]]:
            return True
        else:
            return False
    return False

d = addline({},"Cats Birds donkey Dove camel coffee")
print(spellcheck(d,"donkey"))
print(spellcheck(d,"cats"))
print(spellcheck(d,"Bird"))
print(spellcheck(d,"Birds"))
print(spellcheck(d,"Coffee"))