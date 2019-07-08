def perimeter(n):
    itt = 0
    i=1
    while (i < n+2):
        itt += fibonacci(i)
        i+=1
    its = itt * 4
    return its
def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)