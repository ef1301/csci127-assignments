def encode(input):
    list = []
    count = 0
    for i in range(1,len(input)):
        if input[i-1] == input[i]:
            count += 1
            result = [input[i],count]
        elif input[i-1] != input[i]:
            count = 0
            for i in range(i,len(input)):
                if input[i-1] == input[i]:
                    count += 1
            result = [input[i],count]
    list.append(result)
    return list


##def decode(d):
##    str = []
##    for i in d:
##        val = d[i]
##        reconstruct = val*i
##        str.append(reconstruct)
##    return "".join(str)
print(encode("aaaabb"))
##print(encode("bbbaaaabb"))
##print(encode("abcd"))
##print(encode("cbbbbdee"))

##print(decode(encode("aaaabb")))
##print(decode(encode("bbbaaaabb")))
##print(decode(encode("abcd")))
##print(decode(encode("cbbbbdee")))