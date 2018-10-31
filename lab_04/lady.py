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
                counter[lady.index(i)] += 1
                print(counter)
    return counter
##    
##def happy(n,b): #happiness check
##    if len(b) == 0: #there can't not be anything in the string
##        return False
##    elif len(b) == 1 and b[1] == "_": #if there's only "_" in the string 
##        return True
##    elif "_" not in b: # if "_" isn't in b
##        return False
##    for i in b:
##            position = p.index(i)
            
            
        

##def happyLadybugs(n,b):
##    n = len(b)
    
g = "RBY_YBR"
print(count(g))
##print(happy(5,g))
##print(happyLadybugs(g))