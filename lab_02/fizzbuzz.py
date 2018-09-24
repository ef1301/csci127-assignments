def fizzbuzz(max_value):
    i = 1
    while i <= 100:
        if i == 100:
            print(max_value//15)
        elif (i % 3 == 0) and (i % 5 == 0):
            print("FIZZBUZZ")
        elif i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i = i+1

print(fizzbuzz(100))
#Krystlle Fajardo - fajardokrystlle@gmail.com
#Jadeja Baptiste - dejamax01@gmail.com