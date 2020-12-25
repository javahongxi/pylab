import re

s = 'C|C++|Java|C#|Python|Javascript'

print(s.index('Python') > -1)

print('Python' in s)

# 普通字符
r = re.findall('Python', s)
if len(r) > 0:
    print('字符串中包含Python')

s = 'C0C++7_\tJava8\nC#6\rPython3 Javascript'
# 元字符
# \d \D
# \w \W
# \s \S
r = re.findall('\\d', s)
print(r)
r = re.findall('[0-9]', s)
print(r)
r = re.findall('\s', s)
print(r)

s = 'acc, abc, acd, adf, ccd, afc'
r = re.findall('a[cf]c', s)
print(r)
