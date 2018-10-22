def compress_word(w):
    new = []
    vowels = ["a", "e", "i", "o", "u"]
    new.append(w[:1])
    for i in w[1:]:
        if not i in vowels:
            new.append(i)
    return "".join(new)
print(compress_word("halloween"))
print(compress_word("Special"))
print(compress_word("apple"))


def sentence(line):
    new = []
    sep = line.split(" ")
    for str in sep:
        new_str = compress_word(str)
        new.append(new_str)
    return " ".join(new)

print(sentence("I like to eat apple pie"))
print(sentence("who is there"))