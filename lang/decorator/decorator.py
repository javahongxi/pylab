import time


def log(func):
    def wrapper(*args, **kw):
        print(time.time(), func, args, kw)
        func(*args, **kw)
    return wrapper


@log
def f():
    pass


@log
def f1(param1):
    pass


@log
def f2(param1, param2):
    pass


@log
def f3(param1, param2, **kw):
    pass


f()
f1("a")
f2("b", "c")
f3("d", "e", x="1", y="2")
