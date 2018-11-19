def encode(input):
    d = {}
    for item in input:
        d.setdefault(item,0)
        if item in d:
            d[item] += 1
    return d

print(encode("aaaabb"))
print(encode("bbbaaaabb"))
print(encode("abcd"))
print(encode("cbbbbdee"))