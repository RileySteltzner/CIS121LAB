def letter_count(word):
    letter_count_dict = {}
    for each_letter in word:
        if each_letter not in letter_count_dict:
            letter_count[each_letter] = 1
        else:
            letter_count[each_letter] += 1
    return letter_count_dict