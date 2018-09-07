#Warmp-1:sleep_in
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
#Warmup-1:monkey_trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False
print(monkey_trouble(True, False))
print(monkey_trouble(False, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, True))
#Warmup-1: sum_double
def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = sum*2
  return sum
#Warmup-1: diff21
def diff21(n):
  subtract= abs(n-21)
  if n>21:
    subtract=2*subtract
  return subtract
print(diff21(58))
print(diff21(2))
#Warmup-1:parrot_trouble
def parrot_trouble(talking, hour):
  if talking:
    if hour<7:
      return True
    if 7<=hour<=20:
      return False
    if hour>20 and hour !=20:
      return True
  else:
    return False
print(parrot_trouble(True,6))
print(parrot_trouble(True,7))
print(parrot_trouble(False, 6))
print(parrot_trouble(True,21))
print(parrot_trouble(True, 20))
#Warmup-1:makes10
def makes10(a, b):
  if a==10 or b==10:
    return True
  if a + b ==10:
    return True
  else:
    return False
print(makes10(9,10))
print(makes10(9,9))
print(makes10(7,3))
#Warmup-1:near_hundred
def near_hundred(n):
  if (abs(100-n) <= 10) or (abs(200-n) <= 10):
    return True
  else:
    return False
print(near_hundred(93))
print(near_hundred(111))
print(near_hundred(-50))
print(near_hundred(290))
print(near_hundred(191))
#Warmup-1:pos_neg
def pos_neg(a, b, negative):
  if negative:
    return (a <0 and b<0)
  else:
    return ((a<0 and b>0) or (a>0 and b<0))
#Warmup-1:not_string
def not_string(str):
  if len(str) >= 3 and str[:3] =="not":
    return str
  return "not " + str
print(not_string("not bad"))
print(not_string("a cat"))
#Warmup-1:missing char
def missing_char(str, n):
  front = str[:n]
  back = str[n+1:]
  return front + back
print(missing_char("kitten", 4))
#Warmup-1:front_back
def front_back(str):
  if len(str) <= 1:
    return str
  mid=str[1:len(str)-1]
  return str[len(str)-1] + mid +str[0]
print(front_back("code"))
#Warmup-1:front3
def front3(str):
  str=str[:3]
  return str+str+str
print(front3("boat"))
#String-1:hello_name
def hello_name(name):
  return "Hello "+ name + "!"
print(hello_name("Bob"))
print(hello_name("Alice"))
print(hello_name("X"))
#String-1make abba
def make_abba(a, b):
  return a + b + b + a
print(make_abba('Hi','Bye'))
print(make_abba('Yo','Alice'))
print(make_abba('What','Up'))
#String-1:make_tags
def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"
print(make_tags('i', 'Yay'))
print(make_tags('i', 'Hello'))
print(make_tags('cite', 'Yay'))
#String-1:make_out_word
def make_out_word(out, word):
  if len(out)==4:
    first=out[:2]
    last=out[2:]
  return first + word + last
print(make_out_word("<<>>","Same"))
#String-1:extra_end
def extra_end(str):
  ends=str[-2:]
  return ends + ends + ends
print(extra_end("Hello"))
#String-1:first_two
def first_two(str):
  first = str[:2]
  return first
print(first_two("abcde"))