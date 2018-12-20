def canMakeWord(letters,word):
    l = []
    for item in letters:
        l.append(letters.count(item))
    return l
##    count = len(word)
##    for item in letters:
##        if count == 0:
##            return True
##        if item in word:
##            count = count -1
##        else:
##            continue
##    return False
print(canMakeWord("ladilmy","daily"))
print(canMakeWord("eerriinn","eerie"))
