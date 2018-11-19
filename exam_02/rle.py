def encode(input):
    list = []
    count = 0
    for i in range(1,len(input)):
        if input[i-1] == input[i]:
            count += 1
            print(input[i-1],input[i])
            print(count)
        else:
            return list
        list = [input[i] ,count]
    return list

def decode(d):
    str = []
    for i in d:
        val = d[i]
        reconstruct = val*i
        str.append(reconstruct)
    return "".join(str)
print(encode("aaaabb"))
##print(encode("bbbaaaabb"))
##print(encode("abcd"))
##print(encode("cbbbbdee"))

##print(decode(encode("aaaabb")))
##print(decode(encode("bbbaaaabb")))
##print(decode(encode("abcd")))
##print(decode(encode("cbbbbdee")))