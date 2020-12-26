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

s = 'python 111java678php'
r = re.findall('[a-z]{3,6}', s) # 贪婪
print(r)
r = re.findall('[a-z]{3,6}?', s) # 非贪婪
print(r)

s = 'pytho0python1pythonn2'
r = re.findall('python*', s)
print(r)
r = re.findall('python+', s)
print(r)
r = re.findall('python?', s)
print(r)

s = '100001'
r = re.findall('^\\d{4,8}$', s)
print(r)

s = 'PythonPythonPythonPythonPython'
r = re.findall('(Python){3}', s)
print(r)

s = 'PythonC#\nJavaPHP'
r = re.findall('c#.{1}', s, re.I | re.S)
print(r)

s = 'PythonC#JavaPHPC#'
r = re.sub('C#', 'GO', s, 0)
print(r)
s = s.replace('C#', 'GO')
print(s)


# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\\d+)', double, s))

print(re.match('\\d', s)) # 从首字母开始匹配
r = re.search('\\d', s)
print(r)
print(r.span())
print(r.group())

s = 'life is short, i use python, i love python'
r = re.search('life(.*)python(.*)python', s)
print(r.group(0))
print(r.group(1))
print(r.group(2))
print(r.group(1, 2))
print(r.groups())
