def createCounter():
    i = 0
    def counter():
        nonlocal i
        i = i + 1
        return i
    return counter

def createCounter2():
    def g():
        n = 0;
        while True:
            n = n + 1
            yield n
    it = g()
    def counter():
        return next(it)
    return counter


def createCounter3():
    i = [0]
    def counter():
        i[0] = i[0] + 1
        return i[0]
    return counter

f = createCounter3()
print(f())
print(f())
print(f())
