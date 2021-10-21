def my_zip(*args):
    iterators = [iter(iterator) for iterator in args]
    while True:
        ans = []
        for iterator in iterators:
            try:
                ans.append (next(iterator))
            except:
                return
        yield tuple(ans)

names = ["Alex", "Bob", "Alice", "John", "Ann", "Diana"]
age = [25, 17, 34, 24]
sex = ["M", "M", "F", "M", "F"]

for values in my_zip(names, age, sex):
    print("name: {:>10} age: {:3} sex: {:2}".format(*values))


def my_map(function, iterable):
    iterable = iter(iterable)
    while True:
        try:
            yield (function(next(iterable)))
        except:
            return
arr = [-5, -6, 8, -10, 0]
for i in my_map(abs, arr):
    print (i, end = ' ')
print ()
def my_enumerate(iterable, start=0):
    iterable = iter(iterable)
    while True:
        for i in iterable:
            yield (start, i)
            start+=1

names = ["Alex", "Bob", "Alice", "John", "Ann"]

for idx, elem in my_enumerate(names, 2):
    print("{:02}: {:>7}".format(idx, elem))



'''
output:
name:       Alex age:  25 sex: M
name:        Bob age:  17 sex: M
name:      Alice age:  34 sex: F
name:       John age:  24 sex: M
5 6 8 10 0
02:    Alex
03:     Bob
04:   Alice
05:    John
06:     Ann
'''
