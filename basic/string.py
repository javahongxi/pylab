s = 'Hello, China!'

print(type(s))
print('len: ' + str(len(s)))
print('s[0]: ' + s[0])
print('s[0:5]: ' + s[0:5])
print('s[0:20]: ' + s[0:20])
print('s[7:]: ' + s[7:])
print('s[:5]: ' + s[:5])
print('s[0:-1]: ' + s[0:-1])
print('s[-2:-1]: ' + s[-2:-1])
print('s[:-1]: ' + s[:-1])
print('s[-1:]: ' + s[-1:])

s += ' 2020'
print(s)

s += '\n'
s *= 3
print(s)

city = "Xi'an"
print(city)
city = 'Xi\'an'
print(city)
city = 'Xi\\\'an\\n'
print(city)
city = r'Xi\'an'
print(city)

words = """今天只有残留的躯壳
迎接光辉岁月"""
print(words)
print("风雨中抱紧自由")
