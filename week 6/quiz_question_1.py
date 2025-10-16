def every_other_letter(word):
    results = []
    for i in range(len(word)):
        if i % 2 == 0:
            results.append(word[i])
    return results
user_word = input("Enter a word: ")
print(every_other_letter(user_word))