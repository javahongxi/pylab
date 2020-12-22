t = (1, 'A', True)

print(type(t))
print('len: ' + str(len(t)))
print('l[0]: ' + str(t[0]))
print(t[0:2])

t += (2020,)
t += ('A', 1)
print(t)

# t[0] = 2 invalid
