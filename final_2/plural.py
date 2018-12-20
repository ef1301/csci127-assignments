def countPlurals(line):
    split = line.split()
    count = 0
    for item in split:
        if item[-1] == 's':
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
        if item[-1] == "s":
##            print(item[-2:len(item)])
            if item[-2:len(item)] != "'s":
                count += 1
        else:
            continue
    return count
print(notPossesive("dog's cats bird tree's"))
print(notPossesive("desks chair's boxes head shoulder's"))
print(notPossesive("desk chair's boxes heads snake's"))