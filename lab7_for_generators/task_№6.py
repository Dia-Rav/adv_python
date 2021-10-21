from itertools import accumulate

def maximize(lists, m):
    squared_maxes = [max(lst)**2 for lst in lists]
    polynomials = list(accumulate(squared_maxes))
    return polynomials[-1]%m

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
print (maximize(lists, m=1000))
#206
