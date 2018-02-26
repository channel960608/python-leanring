a = list(map(lambda x:x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a)

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
L2 = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print(L)
print(L2)
