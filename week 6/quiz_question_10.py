def war_of_numbers(numbers):
    odd_total = 0
    even_total = 0
    for n in numbers:
        if n % 2 == 0:
            even_total += n
        else:
            odd_total += n
    if even_total > odd_total:
        return 'Even is the winner!'
    elif odd_total > even_total:
        return 'Odd is the winner!'
    else:
        return "TIE!"
print (war_of_numbers([1,2,3,4,5,6]))
    
