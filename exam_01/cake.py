def divide(A,B,u):
    fraction = A/B
    ratio = fraction.as_integer_ratio()
    people = ratio[1]
    return people
print(divide(5,10,1))