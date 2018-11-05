#EMILY FANG AND RACHIEL TIEU
import random
ADJECTIVES = ["questionable", "delicious", "determined"] # adjectives list
VERBS = ['ate','walked', 'fought', 'rode'] # verbs list
NOUNS = ['dog','sandwich','cat','food','frog', 'sunset'] # nouns list
HEROS = ['Spiderman', 'Hulk', 'Flash'] #heros list
sentence = "<HERO> <VERB> the <ADJECTIVE> <NOUN> and then <HERO> <VERB> the <NOUN> later. Suddenly, a <NOUN> <VERB> a <ADJECTIVE> <NOUN> to town." #sentence

def madlib(s):
#def madlibs(sentence,nouns,verbs):
#stylistically it'd be best to put the lists in here such that they only exist in here
    new_list = [] #empty list that will have strings added to it and returned
    H_random = random.choice(HEROS) # a hero is randomly taken from the heros list, is assigned to H_assign, and remains that value
    for item in s.split(): #for each item in the list
        #s.split splits the string sentence such that it doesn't filter through each character. it filters throught each word
        if item == "<NOUN>": # if the item is <NOUN>
            new_list.append(random.choice(NOUNS)) #a noun will be randomly taken from the NOUNS list and appended to the new list
        elif item == "<VERB>": # if the item is <VERB>
            new_list.append(random.choice(VERBS)) #a verb will be randomly taken from the VERBS list and appended to the new list
        elif item == "<ADJECTIVE>": # if the item is <NOUN>
                new_list.append(random.choice(ADJECTIVES))
        elif item == "<HERO>": # if the item is <HERO>
            new_list.append(H_random) # the H_random value initially assigned to H_random will be appended to the new list
        else: # otherwise 
            new_list.append(item) # the item will be appended
    return " ".join(new_list) # just to make the returned list nicer. takes the new list's strings and combines them with a space in between
print(madlib(sentence)) # print statement

# instead of random.choice you could do NOUNS[random.randrange(0,len(NOUNS))]
#pass is a null operation -- when it is executed, nothing happens. It is useful as a placeholder
#when a statement is required syntactically, but no code needs to be executed

#new_list = "" as a string
#...
#else new_list = new_list + " " + item combining strings