import random
def build_list(size,max_value):
    """
    Create a list of 100 items. Each item should be a random value
    between 1 and 10.
    """
    l1 = []
    for i in range(size):
        l1.append(random.randrange(0,max_value))
        i += 1
    return l1
def max(l):
    """
    Write a routine max(l) which will return the index of an element with
    the largest value in the list. It can be any occurrence.
    """
    lv = 0
    for i in range(1,len(l)):
        if l[i] > l[lv]:
            lv = i
    return lv


def freq(list,val):
    i = 0
    for i in list:
        if val == i:
            i += 1
    return i

l = build_list(100,11)
print("List: " , l)
print("Max: " , max(l))
print("Frequency: " , freq(l,2))