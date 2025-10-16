def user_letter(letter):
    vowels = ['a', 'e','i', 'u']
    if letter in vowels:
        return 'Vowel'
    else:
        return 'Con'
print(user_letter('z'))