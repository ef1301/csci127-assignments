def compress_word(w):
    new = []
    vowels = ["a", "e", "i", "o", "u"]
    lower = w.lower()
    
    for i in w:
        if not i in vowels:
            new.append(i)
            join = "".join(new)

    return join
print(compress_word("halloween"))
print(compress_word("Special"))
print(compress_word("apple"))


def sentence(line):
    new = []
    sep = line.split(" ")
    for str in sep:
        word = compress_word(str)
        new.append(word)
    return " ".join(new)
print(sentence("I like to eat pie"))
print(sentence("who is there"))