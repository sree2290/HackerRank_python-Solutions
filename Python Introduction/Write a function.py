def is_leap(year):
    if (year%400) == 0:
        return True
    if (year%100) == 0:
        return False
    if (year%4) == 0:
        return True
    else:
        return False
    # Write your logic here

    return leap
