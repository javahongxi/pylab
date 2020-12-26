
list_x = [1, 2, 3, 4, 5]
list_y = [1, 2, 3, 4, 5]


def square(x):
    return x * x


r = map(square, list_x)
print(list(r))

r = map(lambda x, y : x * x + y * y, list_x, list_y)
print(list(r))
