#Warmp-1:sleep_in
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
#Warmup-1: sum_double
def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = sum*2
  return sum
#hello_name
def hello_name(name):
  return "Hello "+ name + "!"
print(hello_name("Bob"))
print(hello_name("Alice"))
print(hello_name("X"))
#make abba
def make_abba(a, b):
  return a + b + b + a
print(make_abba('Hi','Bye'))
print(make_abba('Yo','Alice'))
print(make_abba('What','Up'))
#make_tags
def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"
print(make_tags('i', 'Yay'))
print(make_tags('i', 'Hello'))
print(make_tags('cite', 'Yay'))