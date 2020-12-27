
def gen(max):
    n = 0
    while n <= max:
        n += 1
        yield n


g = gen(10000)
print(next(g))
print(next(g))
print(next(g))

n = (i for i in range(0, 10000))
print(n)
