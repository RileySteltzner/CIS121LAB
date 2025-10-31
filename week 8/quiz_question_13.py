def is_vowel(letter):
    return letter.lower() in 'aeiou'
def report_vowels(word):
    vowels = []
    for letter in word:
        if is_vowel(letter):
            vowels.append(letter)
    return vowels
print(report_vowels("apple"))