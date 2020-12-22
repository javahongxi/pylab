info = {"name": "Lily", "age": 24}

print(type(info))
print('len: ' + str(len(info)))
print(info["name"])
info["age"] = 25
print(info)

for k in info:
    print(info[k])
