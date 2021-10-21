
def print_map(function, iterable):
    print (*map(function, iterable), sep = '\n')

arr = [-0.1, 1.3, -4.5, -2.3, 9.0]
print_map (abs, arr)


#out:
#0.1
#1.3
#4.5
#2.3
#9.0
