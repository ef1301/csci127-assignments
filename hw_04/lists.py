#Emily Fang & Darren Liang
import random

def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the lsit
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list

    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l
print(build_random_list(3,100))

l = [3, 2, 3]

def locate(l,value):
    i = 0
    while i < len(l):
        if l[i] == value:
            return i
        else:
            i += 1
    return -1
print(locate(l,3))
print(locate(l,5))

def count(l,value):
    counter = 0
    i = 0
    while i < len(l):
        if l[i] == value:
            counter += 1
        i += 1
    return counter
print(count(l,2))

def reverse(l):
    return l[::-1]
print(reverse(l))

def isIncreasing(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True
print(isIncreasing(l))

def palindrome(l):
    if l[::-1] == l:
        return True
    else:
        return False
print(palindrome(l))
