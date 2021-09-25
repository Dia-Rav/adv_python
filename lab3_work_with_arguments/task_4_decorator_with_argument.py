import time 
def decorator_maker(decorator_arg1):
    def my_decorator(func):
        def wrapped(x, **show):
            LOGGER_FORMAT = '''\
                
            '''
            
            start = time.time()
            ans = func(x, **show)
            end = time.time()
            
            with open(decorator_arg1, 'w') as file:
                file.writelines(
                    'Start time: {start_time} \n Args: {args} \n {return_value} \n End time: {end_time} \n Execution time: {exec_seconds} seconds'.format(
                        start_time=start, 
                        args=x,
                        return_value=('-' if not ans else 'Return: {}'.format(ans)), 
                        end_time=end,
                        exec_seconds=round((end - start), 5)
                    )
                )
            return ans
        return wrapped
    return my_decorator

@decorator_maker('output.txt')
def decorated_function(n, show=False):
    if show:
        a = [0,1]
        for i in range(2, n+1):
            a.append (a[i-2]+a[i-1])
        return a[n]
    a = [0,1]
    for i in range(2, n+1):
        a.append (a[i-2]+a[i-1])
    return
decorated_function(1000)
# при вводе decorated_function(10, show=True) печатает результат 

