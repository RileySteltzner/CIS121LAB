word = ""

while True:
    letter = input("Enter a single letter or type 'done' to finish: ")
    if letter.lower() == 'done':
        break 
    if len(letter) != 1:
        print("Enter a single letter or type 'done' when you want to finish: ")
        continue
    word += letter
print (f'{word}')
