def count(str):
##    lady = [] # stores the different color variables
##    counter = [] # stores the occurances of each color variable in the order of the lady bucket
    d = {}
    for i in str: # runs through each item in the parameter string
        if i != "_": # as long as i is not underscore
            if i not in d: # if the i is not in the lady bucket
##                lady.append(i) # add i to the lady bucket
##                counter.append(1) # add 1 t the counter bucket to begin the count and create the range
                d[i] = 1
            else: #otherwise
                d[i] += 1 #adds 1 to each occurance of i at the index of i
    return d

def happy(n,str):
    if n < 3: #if the length is less than 3 (if length is 2,1,0)
        if n == 0: #the string can't have nothing in it
            return False
        elif n == 1 and str[0] == "_": #if only an empty cell
            return True
        elif n ==2 and str[0] == str[1]: #if the first is the same as the second
            return True
        else:
            return False
    else: # if length is greater than 3 and "_" in b
        d = dict(count(str)).values()
        if min(d) < 2:
            return False
        elif "_" not in str and min(d) >= 2:
            for i in range(1,n):
                if str[i] == str[i+1] and str[i] == str[i-1]:
                    return True
                else:
                    return False
        elif min(d) >= 2 and "_" in str:
            return True
        return True

def happyLadybug(n,b):
    if happy(n,b) == True: #if happy/True
        return "YES"
    elif happy(n,b) != True:
        return "NO"
    
def test(n,b):
    return happyLadybug(n,b)

print(1, test(7,"RBY_YBR"), "YES")
print(2, test(6,"X_Y__X"), "NO")
print(3, test(6,"B_RRBR"), "YES")
print(4, test(5,"AABBC"), "NO")
print(5, test(7,"AABBC_C"), "YES")
print(6, test(4,"AABB_"), "YES")
print(7, test(2,"RX"), "NO")
print(8, test(0,""), "NO")
print(9, test(1,"_"), "YES")
print(10, test(2,"__"), "YES")
print(11, test(10,"DD__FQ_QQF"), "YES")
print(12, test(3,"DD_"), "YES")
print(13, test(2,"DD"), "YES")
print(14, test(4,"QAQA"), "NO")
print(16, test(9,"QQAABBCCC"), "YES")
print(17, test(9,"QAQABB_CC"), "YES")
