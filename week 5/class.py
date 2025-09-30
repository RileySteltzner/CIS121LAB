#write a code to determine how many letters are in a word
'''
word = 'hello world'

count = 0

for letter in word:
    if letter != ' ':
        count += 1
print(count)
'''
#write code to determine how many vowels are in a given code
'''
word1 = 'hello world'
count1 = 0 
for letter in word1:
    if letter in ('a', 'e', 'i', 'o', 'u', 'y'):
        count1 += 1 
print(f'The vowels in {word1} is {count1}')

word2 = 'apples and bananas'
count2 = 0 
for letter in word2:
    if letter in ('a', 'e', 'i', 'o', 'u', 'y'):
        count2 += 1 
print(f'The vowels in {word2} is {count2}')

word3 = 'happy times'
count3 = 0 
for letter in word3:
    if letter in ('a', 'e', 'i', 'o', 'u', 'y'):
        count3 += 1 
print(f'The vowels in {word3} is {count3}')
'''
#word 1 = hello world
#word 2 = apples and bananas
#word 3 = happy times

def vowel_counter(passed_word):
    count = 0
    for letter in passed_word:
        if letter in ('a', 'e', 'i', 'o', 'u', 'y'):
            count += 1 
    print(count)

word1 = 'hello world'
word2 = 'apples and bananas'
word3 = 'happy times'
vowel_counter(word1)
vowel_counter(word2)
vowel_counter(word3)