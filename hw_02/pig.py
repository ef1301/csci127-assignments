#Names: Emily Fang & Matthew Barron
def piglatinfy(name):
    """
    Input: name
    Output: pig_latin
    """
    word = name.lower() # makes the characters in name all lowercase
    firstl = word[0] #word is assigne to the "zeroth"/first character
    vowels = ["a", "e", "i", "o", "u"] #list of vowels assigned to vowels
    end = "ay" #end is assigned to string"ay"
    if firstl in vowels: #if the first letter is in the list vowels
        pig_latin = word + end 
        return pig_latin 
    else: #otherwise
        pig_latin = word[1:] + firstl + end
        return pig_latin
print(piglatinfy("dogs"))
print(piglatinfy("eggs"))
print(piglatinfy("apple"))
print(piglatinfy("octagon"))
print(piglatinfy("umbrella"))
print(piglatinfy("igloo"))
