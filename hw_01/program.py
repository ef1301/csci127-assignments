#CAPITALIZE
def capitalize(name):
    """
    input: name --> a string in the form "first last"
    output: returns a string with each of the two words capitalized
    note: this is the one we started in class
    """
    space_index = name.find(" ")
    first = name[:space_index]
    first = first.capitalize()
    last = name[space_index+1:]
    last = last.capitalize()
    return first + " " + last
print(capitalize("beth sanders"))
    
#INIT    
def init(name):
    """
    Input: name --> a string in the form "first last"
    Returns: a string in the form "F. Last" where it's a capitalized first inital 
    and capitalized last name
    """
    space_index = name.find(" ")
    first = name[:1]
    first = first.capitalize()
    last = name[space_index+1:]
    last = last.capitalize()
    return first + ". " + last
print(init("daniel erwing"))

#PART_PIG_LATIN
def part_pig_latin(name):
    """
    Input: A string that is a single lower case word
    Returns: that string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
    first_letter = name[:1]
    mid_letter = name[1:len(name)-1]
    last_letter = name[len(name)-1:len(name)]
    pig_latin = last_letter + mid_letter + first_letter + "ay"
    return pig_latin
print(part_pig_latin("Hello"))
print(part_pig_latin("Mary"))

#MAKE_OUT_WORD
def make_out_word(out, word): #defined function with input out and word
  if len(out)==4: #if the length of the out input is 4
    first=out[:2] #first is assigned to the first two charaters
    last=out[2:] #last is assigned from the second character to the last
  return first + word + last #return the first 2 chars of out +word +the rest of the out input after the 2nd char
print(make_out_word("<<>>","Same"))

#MAKE_TAGS
def make_tags(tag, word): #defined function with tag and word inputs
  return "<" + tag + ">" + word + "</" + tag + ">" # return tags between "<" & ">" and "</" & ">"
    #in between the tags and their pairs of "<" and ">" word input occurs
print(make_tags('i', 'Yay'))
print(make_tags('i', 'Hello'))
print(make_tags('cite', 'Yay'))

 