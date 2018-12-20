def canMakeWord(letters,word):
    for item in letters:
        if letters.count(item) >= word.count(item):
##            print(letters.count(item) , word.count(item))
            continue
        else:
            return False
    return True
##print("PART 1")
##print(canMakeWord("ladilmy","daily"))
##print(canMakeWord("eerriinn","eerie"))
##print(canMakeWord("orrpgma","program"))
##print(canMakeWord("orppgma","program"))

def withWild(letters,word):
    wild = letters.count("?")
    used = []
    for item in word:
        if item not in used:
            count = letters.count(item)
            if count >= word.count(item):
                continue
            elif count + wild >= word.count(item):
##                print("pass")          
                wild = wild - (word.count(item) - count)
                used.append(item)
                continue
            else:
                return False
        else:
            continue
    return True
print("PART 2")
print(withWild("ladil?","daily"))
print(withWild("eerr??nn","eerie"))
print(withWild("orrpgma","program"))
print(withWild("orppgm","program"))
print(withWild("orppgma?","program"))
print(withWild("orppg???","program"))