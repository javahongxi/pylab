# from enum import Enum
from enum import IntEnum,unique

@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


print(VIP.YELLOW)
print(VIP.YELLOW.name)
print(VIP.YELLOW.value)
print(VIP['YELLOW'])

for v in VIP:
    print(v)

print(VIP.YELLOW == VIP.YELLOW)
print(VIP.YELLOW is VIP.YELLOW)

print(VIP(1))
