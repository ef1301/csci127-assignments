def compress_word(w):
    new = []
    vowels = ["a", "e", "i", "o", "u"]
    new.append(w[:1])
    for i in w[1:]:
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
    print(sep)
    for str in sep:
        new_str = compress_word(str)
        new.append(new_str)
        print(new)
    
print(sentence("I like to eat pie"))
print(sentence("who is there"))