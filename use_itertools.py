import itertools

# natuals = itertools.count(1, 4)
# for n in natuals:
#     print(n)

ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

naturals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, naturals)
print(list(ns))

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
