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


