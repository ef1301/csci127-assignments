def compress_word(w):
    new = []
    vowels = "aeiouAEIOU"
    #rest = word[1:]
# OR vowels = ["a","e","i","o","u","A",..."U"]
    new.append(w[0]) # first letter
    for i in w[1:]:
        if not i in vowels:
            new.append(i)
            #if letter not in vowels:
                #new_rest = new_rest + letter
    return "".join(new)
    #return first + new_rest
print(compress_word("halloween"))
print(compress_word("Special"))
print(compress_word("apple"))
print("Testing compress_word")
print("apple", compress_word("apple"))

def sentence(line):
    new = []
    sep = line.split(" ")
    for str in sep:
        new_str = compress_word(str)
        new.append(new_str)
    return " ".join(new)

print(sentence("I like to eat apple pie"))
print(sentence("who is there"))
#.strip removes unnecessary spaces in the front