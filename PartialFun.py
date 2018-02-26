import functools

def int2_fun(x, base=2):
    return int(x, base)

int2 = functools.partial(int, base=2)
print(int2('1000000'))
