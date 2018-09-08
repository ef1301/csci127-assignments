#Warmp-1:sleep_in
def sleep_in(weekday, vacation): #defined function with inputs weekday & vacation
  if not weekday or vacation: #if it's not a weekday or vacation
    return True 
  else: #otherwise
    return False
#Warmup-1:monkey_trouble
def monkey_trouble(a_smile, b_smile): #defined function with inputs a_smile & b_smile
  if a_smile and b_smile: #if both smile
    return True
  if not a_smile and not b_smile: #if both dont smile
    return True
#insert else statement
  return False
print(monkey_trouble(True, False))
print(monkey_trouble(False, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, True))
#Warmup-1: sum_double
def sum_double(a, b): #defined function with input a & b
  sum = a + b #variable sum (a+b=sum)
  if a == b: #if a and b are equal
    sum = sum*2 #sum variable changes definition/assignment (sum doubles)
  return sum
#Warmup-1: diff21
def diff21(n): #defined function 
  subtract= abs(n-21) #subrtact function created (absolute value of input n-21
  if n>21: #if n is greater than 21
    subtract=2*subtract #subtract assignment changes
  return subtract
print(diff21(58))
print(diff21(2))
#Warmup-1:parrot_trouble
def parrot_trouble(talking, hour): #defined function with inputs with talking and hour
  if talking: #if the parrots are talking
    if hour<7: #if the hour is less than 7
      return True
    if 7<=hour<=20: #if the hour is greater than or equal to 7 and less than or equal to 20
      return False
    if hour>20 and hour !=20: #if hour is greater than 20 and not equal to 20
      return True
  else: #otherwise
    return False
print(parrot_trouble(True,6))
print(parrot_trouble(True,7))
print(parrot_trouble(False, 6))
print(parrot_trouble(True,21))
print(parrot_trouble(True, 20))
#Warmup-1:makes10
def makes10(a, b): #defined function with inputs a and b
  if a==10 or b==10: #if a and b are equal to 10
    return True
  if a + b ==10: #if the sum of a and b is 10
    return True
  else: #otherwise
    return False
print(makes10(9,10))
print(makes10(9,9))
print(makes10(7,3))
#Warmup-1:near_hundred
def near_hundred(n): #defined function with input n
  if (abs(100-n) <= 10) or (abs(200-n) <= 10): #if the absolute value of
      #100-n or 200-n is less than or equal to 10 
    return True
  else: #otherwise
    return False
print(near_hundred(93))
print(near_hundred(111))
print(near_hundred(-50))
print(near_hundred(290))
print(near_hundred(191))
#Warmup-1:pos_neg
def pos_neg(a, b, negative): #defined function with inputs a,b, and negative
  if negative: # if negative is True
    return (a <0 and b<0) #a and b are negactive
  else: #Otherwise
    return ((a<0 and b>0) or (a>0 and b<0)) #either a or b is negative
#Warmup-1:not_string
def not_string(str): #defined function with inut str/string
  if len(str) >= 3 and str[:3] =="not": # if the character count is greater than or equal to 3
      #and the first 3 characters is "not"
    return str
  return "not " + str
print(not_string("not bad"))
print(not_string("a cat"))
#Warmup-1:missing char
def missing_char(str, n): #defined function with input str and n
  front = str[:n] #defined front from the first character to the nth character in the sequence
  back = str[n+1:] #defined back from n+1 to the end
  return front + back #combine front and back
print(missing_char("kitten", 4))
#Warmup-1:front_back
def front_back(str): #defined function with input str
  if len(str) <= 1: #if the length of the string is less than or equal to 1
    return str
  mid=str[1:len(str)-1] # defined mid as in between the 
  return str[len(str)-1] + mid +str[0]
print(front_back("code"))
#Warmup-1:front3
def front3(str): #defined function with string input
  str=str[:3] #str is assigned to return the first to third character
  return str+str+str #returned repetition 3 times
print(front3("boat"))
#String-1:hello_name
def hello_name(name): #defined function with name input
  return "Hello "+ name + "!" #return string"Hello" the input and "1"
print(hello_name("Bob"))
print(hello_name("Alice"))
print(hello_name("X"))
#String-1make abba
def make_abba(a, b): #defined functon with inputs a and b
  return a + b + b + a #return a and b in an abba pattern
print(make_abba('Hi','Bye'))
print(make_abba('Yo','Alice'))
print(make_abba('What','Up'))
#String-1:make_tags
def make_tags(tag, word): #defined function with tag and word inputs
  return "<" + tag + ">" + word + "</" + tag + ">" # return tags between "<" & ">" and "</" & ">"
    #in between the tags and their pairs of "<" and ">" word input occurs
print(make_tags('i', 'Yay'))
print(make_tags('i', 'Hello'))
print(make_tags('cite', 'Yay'))
#String-1:make_out_word
def make_out_word(out, word): #defined function with input out and word
  if len(out)==4: #if the length of the out input is 4
    first=out[:2] #first is assigned to the first two charaters
    last=out[2:] #last is assigned from the second character to the last
  return first + word + last #return the first 2 chars of out +word +the rest of the out input after the 2nd char
print(make_out_word("<<>>","Same"))
#String-1:extra_end
def extra_end(str): #defined function with string input
  ends=str[-2:] #assign end to take the last 2 characters
  return ends + ends + ends #ends is duplicated 3 times
print(extra_end("Hello"))
#String-1:first_two
def first_two(str): #defined function with string input
  first = str[:2] #assign first as the first two chars
  return first #return the first 2 chars
print(first_two("abcde"))
#String-1:first_half
def first_half(str): #defined function with string input
  count = len(str) #count is assigned to the length of the string
  a = count//2 #a is assigned to count divied by 2 into an integer value
  half= str[:a] #half is assigned to the first a chars
  return half
print(first_half("cart"))
#String-1:without_end
def without_end(str): #defined function with string input
  second_last= len(str)-1 #second_last is assigned to the value of the length of str minus 1
  a=str[1:second_last] #a is assigned to the string from char 1 to second_last
  return a
print(without_end("dog"))
#String-1:combo_string
def combo_string(a, b): #defined function with inputs a and b
  if len(a) > len(b): #if the length of a is greater ta b
    return b +a +b #return sequence bab
  if len(b) > len(a): #if the length of b is greater than a
    return a + b + a #return sequence aba
print(combo_string("cat", "house"))
print(combo_string("house", "cat"))
#String-1:non_start
def non_start(a, b): #defined function with inputs a and b
  aa= a[1:] #aa is assigned to the first char of a
  bb= b[1:] #bb is assigned to the first character of b
  return aa + bb #return aa+bb
print(non_start("dog", "cat"))
#String-1:left2
def left2(str): #defined function with string input
  if len(str)>=2: #if the length of the string is greater than or equal to 2
    front=str[:2] #front is assigned to the first 2 chars of the str
    back=str[2:] #back is ssigned to the last 2 chars of the string
    return back + front #return back +front
print(left2("Birds"))
print(left2("bridges"))
#Warmup-2:string_times
def string_times(str, n): #defined function with string input and integer input
  return str*n #str is multiplied or duplicated n times
print(string_times("dog",4))
#Warmup-2:string_times
def front_times(str, n): #defined function with string input and integer input
  a = str[:3] #takes the first 3 character and assigns to a
  return a*n #the first 3 characters are duplicated n times
print(front_times("water", 3))