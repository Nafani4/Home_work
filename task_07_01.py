def fibonacci (num):
    x, y = 0, 1
    for i in range(num):
        x, y = y, x + y
        yield x

if __name__ == '__main__':
    print(fibonacci(10))
    for i in fibonacci(10):
        print(i)