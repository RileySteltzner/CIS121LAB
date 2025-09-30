def convert_knuts(knuts):
    output = " "
    galleon = knuts // (29*17)
    knuts_rem = knuts - (galleon * (29*17))
    sickle = knuts_rem // 29 
    knuts_rem = knuts_rem - (sickle * 29)

    if galleon > 0:
        output = output + f'{galleon} '
    if sickle > 0:
        output = output + f'{sickle} '
    if knuts_rem > 0:
        output = output + f'{knuts_rem} '
    return output
print(convert_knuts(544))
    
