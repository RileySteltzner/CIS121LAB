from random import randint
def coin_toss(guess = 0):
    
    value = randint(0,1)

    if guess == 0 and value == 0:
        return "correct"
    elif guess == 0 and value == 1:
        return "incorrect"
    elif guess == 1 and value == 0:
        return "incorrect"
    elif guess == 1 and value == 1:
        return "correct"

print(coin_toss(1))

