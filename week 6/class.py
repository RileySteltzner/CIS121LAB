

#x = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday']

#print(x[2])
#print(x[1:4])

#for element in x:
#   print(element)

#add saturday and sunday
#print(x)
#x.append('Saturday, Sunday')
#print(x)

#print just nes in string Wednesday
#print(x[2][3:6])

#change Friday to Funday
#print(x)
#x[4] = 'Funday'
#print(x)


#mutable object
#y = x
#print(x)
#print(y)
#x[4] = 'Funday'
#print(x)
#print(y)

#tuple (data, data, data) - immutable list - cannot be changed
#x = ('Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday')

#print(x)
#x[4] = 'Funday'
#print(x)




#write a function that takes a string as an argument, and returns a list containing 
#all of the words in that string

word = 'Peter Piper picked a peck of pickled peppers. '
result = ['Peter', 'Piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers' ]

def string_to_list(word):
    words = []
    built_word = ''
    for letter in word:
        if letter == ' ':
            words.append(built_word)
            built_word = ''
        else:
            built_word += letter
            

    return words
print(string_to_list(word))