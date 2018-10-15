import random
VERBS = ['ate','walked', 'ran', 'skipped'] # verbs list
NOUNS = ['dog','sandwich','cat','food','frog'] # nouns list
HEROS = ['Spiderman', 'Hulk', 'Flash'] #heros list
sentence = "<HERO> <VERB> in the <NOUN> and then <HERO> <VERB> <NOUN> later." #sentence
def madlib(s):
    new_list = [] #empty list that will have strings added to it and returned
    H_random = random.choice(HEROS) # a hero is randomly taken from the heros list, is assigned to H_assign, and remains that value
    for item in s.split(): #for each item in the list
        if item == "<NOUN>": # if the item is <NOUN>
            new_list.append(random.choice(NOUNS)) #a noun will be randomly taken from the NOUNS list and appended to the new list
        elif item == "<VERB>": # if the item is <VERB>
            new_list.append(random.choice(VERBS)) #a verb will be randomly taken from the VERBS list and appended to the new list
        elif item == "<HERO>": # if the item is <HERO>
            new_list.append(H_random) # the H_random value initially assigned to H_random will be appended to the new list
        else: # otherwise
            new_list.append(item) # the item will be appended
    return " ".join(new_list) # just to make the returned list nicer. takes the new list's strings and combines them with a space in between
print(madlib(sentence)) # print statement
