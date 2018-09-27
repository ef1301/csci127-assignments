def mysqrt(n):
    i = 1
    last_digit = n % 10
    while i <= n:
        i = i + 1
        new = (i+ (n/i))/2
        print(new)
print(mysqrt(25))