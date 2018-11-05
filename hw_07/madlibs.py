#EMILY FANG
#WITH DICTIONARIES
import random
d = {}
d['NOUNS'] = ['dog','sandwich','cat','food','frog', 'sunset']
d['ADJECTIVES'] = ["questionable", "delicious", "determined"]
d['VERBS'] = ['ate','walked', 'fought', 'rode']
d['HEROS'] = ['Spiderman', 'Hulk', 'Flash']
sentence = "<HERO> <VERB> the <ADJECTIVE> <NOUN> and then <HERO> <VERB> the <NOUN> later. Suddenly, a <NOUN> <VERB> a <ADJECTIVE> <NOUN> to town." #sentence

def madlib(s,d):
    new_list = [] #empty list that will have strings added to it and returned
    H_random = random.choice(d['HEROS']) # a hero is randomly taken from the heros list, is assigned to H_assign, and remains that value
    for item in s.split(): #for each item in the list
        #s.split splits the string sentence such that it doesn't filter through each character. it filters throught each word
        if item == "<NOUN>": # if the item is <NOUN>
            new_list.append(random.choice(d['NOUNS'])) #a noun will be randomly taken from the NOUNS list and appended to the new list
        elif item == "<VERB>": # if the item is <VERB>
            new_list.append(random.choice(d['VERBS'])) #a verb will be randomly taken from the VERBS list and appended to the new list
        elif item == "<ADJECTIVE>": # if the item is <NOUN>
                new_list.append(random.choice(d['ADJECTIVES']))
        elif item == "<HERO>": # if the item is <HERO>
            new_list.append(H_random) # the H_random value initially assigned to H_random will be appended to the new list
        else: # otherwise 
            new_list.append(item) # the item will be appended
    return " ".join(new_list) # just to make the returned list nicer. takes the new list's strings and combines them with a space in between
print(madlib(sentence,d)) # print statement
