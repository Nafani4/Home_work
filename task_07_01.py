def print_fibonacci(gen):
    lst = []
    for i in gen:
        lst.append(i)
    a = ' '.join([str(i) for i in lst])
    print(a)

def decorator(func):
    def wrapper(*arg,**kwargs):
        gen = func(*arg,**kwargs)
        print_fibonacci(gen)
    return wrapper

@decorator
def fibonacci(x):
    lst = [1, ]
    for i in range(1, x):
        i = lst[i-1]+lst[i-2]
        lst.append(i)
        yield i

fibonacci(10)