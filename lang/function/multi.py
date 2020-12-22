
def address():
    return "China", "Wuhan"


country, city = address()
print(country, city)

# 序列解包
a, b, c = 1, 2, 3
print(a, b, c)
d = 4, 5, 6
a, b, c = d
print(a, b, c)

a = b = c = 1
print(a, b, c)
