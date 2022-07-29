def average(array):
    # your code goes here
    sumarray = sum(set(array))
    leng = len(set(array))
    avg = sumarray/leng
    return avg
