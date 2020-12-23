
class Human:
    # 类变量
    total = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def to_str(self):
        print('parent:', self.name, self.age)