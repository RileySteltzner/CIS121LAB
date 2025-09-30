def user_guess(guess):
    from random import randint
    value = randint(0,1)
    if guess == value:
        return 'CORRECT'
    else:
        return 'INCORRECT'
print (user_guess(0))