def gener_fib (n):
    a, b = 0, 1
    while True:
        yield a
        n -= 1
        a, b = b, a+b
        if n==0:
            break

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
for i in gener_fib(11):
    print(i, end = ' ')
    
    
# output:
#0 1 1 2 3 5 8 13 21 34 55
