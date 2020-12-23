# 类
class Student():
    # 类变量
    total = 0

    # 构造函数
    # self 名字任意
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age
        # 构造函数中访问类变量
        self.__class__.total += 1

    # 实例方法
    def to_str(self):
        print(self.name, self.age)

    # 类方法
    @classmethod
    def print_total(cls):
        # 实例方法中访问类变量
        print('total:', cls.total)
