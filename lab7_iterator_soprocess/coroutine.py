import numpy as np


class PrintVariance(Exception):
    pass


class PrintMean(Exception):
    pass


class PrintCount(Exception):
    pass

def server_coroutine():
    print("Starting coroutine")
    aggregator = []
    try:
        while True:
            try:
                to_add = yield
                aggregator.append(to_add)
            except PrintVariance:
                yield np.var(aggregator)
            except PrintMean:
                yield np.mean(aggregator)
            except PrintCount:
                yield len(aggregator)
    finally:
        print("Stop coroutine")


coroutine = server_coroutine()
next(coroutine)
i = int(input())
while i != 0:
    coroutine.send(i)
    if i % 2 == 0:
        print("Current variance:", coroutine.throw(PrintVariance))
        next(coroutine)
    if i % 3 == 0:
        print("Current mean:", coroutine.throw(PrintMean))
        next(coroutine)
    if i % 5 == 0:
        print("Current count:", coroutine.throw(PrintCount))
        next(coroutine)
    i = int(input())
        

coroutine.close()

'''
Starting coroutine
5
Current count: 1
6
Current variance: 0.25
Current mean: 5.5
4
Current variance: 0.6666666666666666
3
Current mean: 4.5
5
Current count: 5
3
Current mean: 4.333333333333333
2
Current variance: 1.7142857142857142
2
Current variance: 1.9375
30
Current variance: 69.77777777777777
Current mean: 6.666666666666667
Current count: 9
0
Stop coroutine
'''
