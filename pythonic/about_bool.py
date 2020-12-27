
class Test():
    def __len__(self):
        return 0

    def __bool__(self):
        return False


print(bool(None))
print(bool([]))
test = Test()
print(bool(test))
print(len(test))
