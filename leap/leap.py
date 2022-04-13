def leap_year(year):
    leap = True
    if year % 4 != 0:
        leap = False
    elif year % 100 != 0:
        leap = True
    elif year % 400 != 0:
        leap = False
    else: leap = True
    return leap
    #pass
