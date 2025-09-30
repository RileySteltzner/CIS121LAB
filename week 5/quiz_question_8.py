def pool_time(grade, time):
    if grade == 'k':
        grade == 0
    if 0 <= grade <= 3:
        if  time == 'morning':
            return '9am'
        elif time == 'afternoon':
            return '1pm'
    elif 4 <= grade <= 8:
        if time =='morning':
            return '10am'
        elif time == 'afternoon':
            return '2pm'
    elif 9 <= grade <= 12:
        if time == 'morning':
            return '11am'
        elif time == 'afternoon':
            return '3pm'
    else:
        return 'age not in range'
print(pool_time(0, 'morning'))

        