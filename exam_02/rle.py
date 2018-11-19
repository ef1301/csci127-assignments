def encode(input):
    list = []
    count = 1
    for i in range(1,len(input)):
        if input[i] == input[i-1]:
            count += 1
        else:
            result = [input[i-1],count]
            list.append(result)
            count = 1
        result = [input[i],count]
    list.append(result)
    return list


def decode(d):
    str = []
    for i,num in d: 
        reconstruct = i*num
        str += reconstruct
    return "".join(str)

print(encode("aaaabb"))
print(encode("bbbaaaabb"))
print(encode("abcd"))
print(encode("cbbbbdee"))

print(decode(encode("aaaabb")))
print(decode(encode("bbbaaaabb")))
print(decode(encode("abcd")))
print(decode(encode("cbbbbdee")))