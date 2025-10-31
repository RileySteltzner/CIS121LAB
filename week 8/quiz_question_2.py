from random import randint
def user_guess(guess = "even"):
    value = randint(0,9)
    if guess == "even": 
        if value % 2 == 0:
            return "correct"
        else: 
            return "incorrect"
    if guess == "odd":
        if value % 2 != 0:
            return "correct"
        else:
            return "incorrect"
print(user_guess())