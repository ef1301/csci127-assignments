#EMily and Kyra
import random #random module

def build_random_list(size, max_val):
    l = [] #empty list for the randomly enerated values
    for i in range(size): # for each value in the range of the size
        l.append(random.randrange(1,max_val)) #a rancom integer from 1 to the max value is appended to the list
    return l # list is returned


def max(l):
    largest_val = 0 #placeholder
    for i in range(1,len(l)): #for each item in the rang of 1 to the length of l/ the size in function build_random_list
        if l[i]> l[largest_val]: #if the index 1 of l is greater than the largest value placeholder
            largest_val = i # the largest value is reassigned to i
    return largest_val #return the largest value

def freq(l,value):
    save_point = 0 #counter for the value
    for item in l: #for each item in the list
        if value == item: #if the value is equal to the current item
            save_point += 1 #1 is added to the counter
    return save_point #return the counter

def mode(l):
    freq_mode = 0 #allows for reassignment and creates a placeholder
    item_mode = 0 #allows for reassignment and creates a placeholder
    for item in l: # for each item in the list
        current = freq(l,item) #the frequency of the current item being filtered
        if current >= freq_mode: #if the current frequency is grater than the placeholder
           freq_mode = current #current becomes the new place holder
           item_mode = item #the item is recorded 
    return item_mode #the recorded item is returned           

base_l = build_random_list(100,11)
print("This is the list: " , base_l)
print("This is the max value's index: " , max(base_l))
print("This is the frequency of 1: " , freq(base_l,1))
print("This is the frequency of 2: " , freq(base_l,2))
print("This is the frequency of 3: " , freq(base_l,3))
print("This is the frequency of 4: " , freq(base_l,4))
print("This is the frequency of 5: " , freq(base_l,5))
print("This is the frequency of 6: " , freq(base_l,6))
print("This is the frequency of 7: " , freq(base_l,7))
print("This is the frequency of 8: " , freq(base_l,8))
print("This is the frequency of 9: " , freq(base_l,9))
print("This is the frequency of 10: " , freq(base_l,10))
print("This is the mode: " , mode(base_l))