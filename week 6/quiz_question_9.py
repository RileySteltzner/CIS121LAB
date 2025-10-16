def count(list_of_cards):
    points = 0
    for card in list_of_cards:
        if card in [10, 'j', 'q', 'k', 'a']:
            points -= 1
        elif card in [2, 3, 4, 5, 6]:
            points += 1
    return points 
print (count([5,9,10,3,'j', 'a', 4, 8, 5]))