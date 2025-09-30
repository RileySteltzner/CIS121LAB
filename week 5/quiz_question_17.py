def user_letter(letter):
    letters = ['a', 'e','i', 'u']
    if letter in letters:
        return 'Vowel'
    else:
        return 'Con'


print(user_letter('z'))