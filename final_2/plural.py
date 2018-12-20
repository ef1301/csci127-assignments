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
    