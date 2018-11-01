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
#                print(lady)
#                print(counter)
            else: #otherwise
                counter[lady.index(i)] += 1 #adds 1 to each occurance of i at the index of i
#                print(counter)
    return counter

def happy(games,str): #happiness check
    if len(str) < 3: #if the length is less than 3 (if length is 2,1,0)
        if len(str) == 0: #the string can't have nothing in it
            return False
        if len(str) == 1 and str[0] == "_": #if only an empty cell
            return True
        if str[0] == str[1]: #if the first is the same as the second
            return True
        else:
            return False
    elif len(str) >= 3 or "_" in str: # if length is greater than 3 and "_" in b
        check = count(str)
        for i in check:
            if i < 2:
                return False
        return True
##        print(counter)
        pass
    for i in range(0,len(str)):
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
print(8, test(6,""), "NO")
print(9, test(3,"_"), "YES")
print(10, test(3,"__"), "YES")
print(11, test(5,"DD__FQ_QQF"), "YES")
print(12, test(2,"DD_"), "YES")
print(13, test(5,"DD"), "YES")
print(14, test(5,"QQQ_"), "YES")
print(15, test(5,"QQ_QQ"), "YES")