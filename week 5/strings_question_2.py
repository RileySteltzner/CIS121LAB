def is_fever(temperature):
    if temperature[-1] == 'F':
        if temperature < '98.6F':
            return 'False'
        elif temperature > '98.6F':
            return 'True'
    elif temperature [-1] == 'C':
        if temperature < '37C':
            return 'False'
        elif temperature > '37C':
            return 'True'
user_temperature = input("Enter a temp 00F or 00C: ")
print(f"is fever {is_fever(user_temperature)}")