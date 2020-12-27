import time


def f1():
    print("function f1")


def f2():
    print("function f2")


def print_current_time(func):
    print(time.time())
    func()


print_current_time(f1)
print_current_time(f2)
