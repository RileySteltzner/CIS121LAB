def is_isogram(word):
    word = word.lower()
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            return False
        else:
            letter_count[letter] = 1
    return True