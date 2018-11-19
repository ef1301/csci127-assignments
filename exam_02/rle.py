def encode(input):
    list = []
    count = 1
    for i in range(1,len(input)):
        if input[i-1] == input[i]:
            count += 1
            result = [input[i],count]
##            print(result)
        elif input[i-1] != input[i]:
            result = [input[i-1],count]
            list.append(result)
##            print(list)
            count = 0
            for i in range(i,len(input)):
                if input[i-1] == input[i]:
                    count += 1
            result = [input[i-1],count]
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