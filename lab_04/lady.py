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
    if len(str) < 3:
        if len(str) == 0:
            return False
        if str[0] == str[1]:
            return True
        elif len(str) == 1 and str[0] == "_":
            return True
        else:
            return False
    elif "_" in str: # if "_" in b
        check = count(str)
        for i in check:
            if i < 2:
                return False
            else:
                return True
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

print(test(7,"RBY_YBR"))
print(test(6,"X_Y__X"))
print(test(6,"B_RRBR"))
print(test(5,"AABBC"))
print(test(7,"AABBC_C"))
#print(test(6,"AABDBC"))
print(test(2,"RR"))
print(test(6,""))