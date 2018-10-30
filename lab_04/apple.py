def countApplesandOranges(s,t,a,b,m,n):
    sam_apples = 0
    sam_oranges = 0
    
    for item in apples: #for each
        posa = a + item
        if posa in range(s,t+1):
            sam_apples += 1
    for item in oranges:
        posb = b + item
        if posb in range(s,t+1):
            sam_oranges += 1
    print("Sam's apples: ", sam_apples)
    print("Sam's oranges:", sam_oranges)


s,t = [7,11]
a,b = [5,15]
m,n = [3,2]
apples = [-2,2,1]
oranges = [5,-6]

print(countApplesandOranges(s,t,a,b,m,n))