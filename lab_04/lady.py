def count(str):
    lady = [] # stores the different color variables
    counter = [] # stores the occurances of each color variable in the order of the lady bucket
    for i in str: # runs through each item in the parameter string
        if i != "_": # as long as i is not underscore
            if i not in lady: # if the i is not in the lady bucket
                lady.append(i) # add i to the lady bucket
                counter.append(1) # add 1 t the counter bucket to begin the count and create the range
            else: #otherwise
                counter[lady.index(i)] += 1 #adds 1 to each occurance of i at the index of i
    return counter

def happy(games,str):
    if games < 3: #if the length is less than 3 (if length is 2,1,0)
        if games < 2 and str[0] == "_": #if only an empty cell
            return True
        elif str[0] == str[1]: #if the first is the same as the second
            return True
        else:
            return False
    for i in range(0,games):
        if str[i] != str[i+1] or str[i] != str[i-1]:
            return False
    if str[i] != str[i+1] or str[games-1] != str[games-2]:
        return False
    return True

def position_check(games,str):
    if happy(games,str):
        pass
    elif "_" in str: # if length is greater than 3 and "_" in b
        for i in count(str): #checks if count is at least 2 of each letter in the string
            if i < 2: #if count is less than 2
                return False
        return True

def happyLadybug(games,str):
    if position_check: #if happy/True
        pass
    elif position_check != True:
        return "NO"
    return "YES"

def test(games,str):
    return happyLadybug(games,str)

print(1, test(7,"RBY_YBR"), "YES")
print(2, test(6,"X_Y__X"), "NO")
print(3, test(6,"B_RRBR"), "YES")
print(4, test(5,"AABBC"), "NO")
print(5, test(7,"AABBC_C"), "YES")
print(6, test(6,"AABDBC"), "NO")
print(7, test(2,"RX"), "NO")
print(8, test(0,""), "NO")
print(9, test(1,"_"), "YES")
print(10, test(2,"__"), "YES")
print(11, test(10,"DD__FQ_QQF"), "YES")
print(12, test(3,"DD_"), "YES")
print(13, test(2,"DD"), "YES")
print(14, test(4,"QQQ_"), "YES")
print(15, test(5,"QQ_QQ"), "YES")