human_age = float(input("Enter your age: "))
your_dog_age = human_age * 7
years = int(your_dog_age)
dog_months = (your_dog_age - years)*12
months = int(dog_months)
days = int((dog_months - months)*30)



print(f'You are {years} years {months} months {days} days as a dog. ')
