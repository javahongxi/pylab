l = [1, 'A', True]

print(type(l))
print('len: ' + str(len(l)))
print('l[0]: ' + str(l[0]))
print(l[0:2])

l += [2020]
print(l)

l[0] = 2
print(l)

m = [2, 'A', True, 2020]
print(l == m)