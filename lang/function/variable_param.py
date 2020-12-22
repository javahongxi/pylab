
def demo(x, *param):
    print(type(param))
    print(x)
    print(param)


def squsum(*numbers):
    sum = 0
    for i in numbers:
        sum += i * i
    return sum


def city_temp(**param):
    print(type(param))
    for c, t in param.items():
        print(c, ':', t)


demo(1, 2, 3, 4)

a = (5, 6, 7, 8)
demo(*a)

demo(100)

print(squsum(1, 2, 3))

city_temp(bj='32c', xm='23c', sh='31c')
b = {'bj': '32c', 'xm': '23c', 'sh': '31c'}
city_temp(**b)
