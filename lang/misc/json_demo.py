import json

s = '{"name":"lily", "age":24, "flag":true}'

user = json.loads(s)
print(type(user))
print(user)
print(user['name'])

s = '[{"name":"lily", "age":24, "flag":true}, {"name":"lucy", "age":25}]'

users = json.loads(s)
print(type(users))
print(users)

print(json.dumps(users))
