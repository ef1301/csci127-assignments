def compress_word(w):
    new = []
    vowels = ["a", "e", "i", "o", "u"]
    lower = w.lower()
    new.append(w[0])
    for i in w[1:]:
        if not i in vowels:
            new.append(i)
            join = "".join(new)
    return join
print(compress_word("halloween"))
print(compress_word("Special"))
print(compress_word("apple"))

