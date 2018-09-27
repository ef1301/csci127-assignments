def mysqrt(n):
    i = 1
    while i <= n:
        new = (i+ (n/i))/2
        if round(new*new) == n:
            return(new)
        else:
            print(new)
        i += 1
print(mysqrt(25))