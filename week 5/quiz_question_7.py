def resting_heart_rate(age, ath_goal):
    if 20 <= age <= 39:
        if ath_goal == 'above average':
            return '47-72'
        elif ath_goal == 'below average':
            return '73-93'
    elif 40 <= age <= 59:
        if ath_goal == 'above average':
            return '46-71'
        elif ath_goal == 'below average':
            return '72-94'
    elif 60 <= age <= 79:
        if ath_goal == 'above average':
            return '45-70'
        elif ath_goal == 'below average':
            return '71-97'
    else:
        return 'age not in range'
print(resting_heart_rate(42, 'below average'))