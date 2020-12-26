from functools import reduce

# 连续计算，连续调用lambda
list_x = [1, 2, 3, 4, 5]
r = reduce(lambda x, y : x + y, list_x)
print(r)
