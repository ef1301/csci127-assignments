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
