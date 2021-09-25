def swap (func):
    def new_div(*arguments,  **show):
        arg = reversed(arguments)
        func(*arg, **show )
    return new_div

@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

print(div(10, 5, show=True))
#output = 0.5
