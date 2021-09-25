import sys
import argparse

def fib(n):
    a = [0,1]
    for i in range(2, n+1):
        a.append (a[i-2]+a[i-1])
    return a[n]


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n')
    return parser


if __name__ == '__main__':
    try:
        print(fib(int(sys.argv[1])))
    except:
        parser = createParser()
        namespace = parser.parse_args()
        print(fib(int(namespace.n)))
