#write a function that returns a dictionary containing how many times 
#each letter appears
'''
def letter_counter(word):
    letter_dictionary = {}
    for letter in word:
        if letter in letter_dictionary:
            #add in key value pair. What are key and value?
            letter_dictionary[letter] = letter_dictionary + 1
        else: # key is not in dictionary
            letter_dictionary[letter] = 1
    return letter_dictionary
#my_word = 'Peter piper picked a peck of pickled peppers'
print (letter_counter('Peter piper picked a peck of pickled peppers'))
'''


def add_three(x):
    y = x + 3
    return y 
var0 = 7 
var1 = add_three(var0)
print(var1)