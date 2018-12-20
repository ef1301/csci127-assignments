def canMakeWord(letters,word):
    for item in letters:
        if letters.count(item) >= word.count(item):
##            print(letters.count(item) , word.count(item))
            continue
        else:
            return False
    return True
print(canMakeWord("ladilmy","daily"))
print(canMakeWord("eerriinn","eerie"))
print(canMakeWord("orrpgma","program"))

