def count(str):
    """
    Utilizes 'buckets' to store information: the different colors and how
    many times they occur in a string.
    """
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

def happy(games,str): #happiness check
    if games < 3: #if the length is less than 3 (if length is 2,1,0)
        if games == 0: #the string can't have nothing in it
            return False
        elif games == 1 and str[0] == "_": #if only an empty cell
            return True
        elif str[0] == str[1]: #if the first is the same as the second
            return True
        else:
            return False
    elif games >= 3: # if length is greater than 3 and "_" in b
        for i in count(str):
            if i < 2:
                return False
        return True
    for i in range(0,games):
        if i>0 and str[i] != str[i-1]:
            return False
        elif str[i] != str[i+1]:
            return False
    return True

def happyLadybug(games,str):
    if happy(games,str) == True: #if happy/True
        pass
    elif happy(games,str) != True:
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