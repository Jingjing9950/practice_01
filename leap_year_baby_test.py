def is_leap_baby(day,month,year):
    # Write your code after this line.
    if year %4 == 0 and year != 1900 and month ==2 and day == 29:
        return True
    else:
        return False

print (is_leap_baby(29,2,1996))