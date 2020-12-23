c = 50


def add(x, y):
    c = x + y
    print(c)


def demo():
    d = 50
    # python 没有块级作用域
    for i in range(0, 9):
        a = 'a'
        d += 1
    if d > 50:
        b = 'b'
    print(d)
    print(a) # OK
    print(b) # OK


add(1, 2)
print(c)
demo()