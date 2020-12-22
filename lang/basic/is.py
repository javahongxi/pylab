m = 1
n = 1.0
print(m == n) # value
print(m is n) # mem address

print(id(m))
print(id(n))

print(m is not n)

a = {1, 2, 3}
b = {2, 1, 3}
print(a == b)
print(a is b)

c = (1, 2, 3)
d = (2, 1, 3)
print(c == d)
print(c is d)
