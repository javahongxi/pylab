# 类
class Student():
    # 类变量
    total = 0

    # self 名字任意
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age
        # 构造函数或实例方法中获取类变量
        print(self.__class__.total)

    def to_str(self):
        print(self.name, self.age)
