print("Enter a number. I will divide 10 by that number, and output the remainder. ")
user_input = input("your number: ")

try:
    user_number = int(user_input)
    results = 10 / user_number
    print(f"The result is {results}")
except ValueError:
    print("dont use letters")

except ZeroDivisionError:
    print("dont pick 0")


