# 列表推导式

a = [1, 2, 3, 4]
b = [i**2 for i in a if i > 1]
print(b)

a = {1, 2, 3, 4}
b = {i**2 for i in a if i > 1}
print(b)

info = {"one": "first", "two": "second"}
b = {value:key for key,value in info.items()}
print(b)
