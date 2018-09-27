#Emily Fang
#Rachel Tieu
def mysqrt(n):
    i = 1
    oldguess = 1
    while i <= n:
        new = (oldguess+ (n/oldguess))/2
        print(oldguess, new)
        if oldguess == new:
            break
        oldguess = new
print(mysqrt(3))
print(mysqrt(100))

#old inaccurate code
#def mysqrt(n):
#    i = 1
#    while i <= n:
#        new = (i+ (n/i))/2
#        if round(new*new) == n:
#            return(new)
#        else:
#            print(new)
#        i += 1
#print(mysqrt(3))
