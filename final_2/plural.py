def countPlurals(line):
    split = line.split()
    count = 0
    for item in split:
        if item[len(item)-1] == 's':
            count += 1
        else:
            continue
    return count
print(countPlurals("dogs cats bird tree"))
print(countPlurals("desks chairs boxes head shoulders"))

def notPossesive(line):
    split = line.split()
    count = 0
    for item in split:
        if item[len(item)-2:len(item)-1] == "'s":
            continue
        elif item[len(item)-1]== "s":
            count += 1
    return count
print(notPossesive("dog's cats bird tree's"))
print(notPossesive("desks chair's boxes head shoulder's"))
    