cities = {'Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen'}

print(type(cities))
print('len: ' + str(len(cities)))
others = {'Wuhan', 'Shanghai'}
all = cities.union(others)
print(all)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)
print(a & b)
print(a | b)
print(a ^ b)

c = {'x', 'y'}
d = {'y', 'x'}
print(c == d)
