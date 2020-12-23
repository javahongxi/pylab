from human import Human


# 类
class Student(Human):

    # 构造函数
    # self 名字任意
    def __init__(self, name, age, school):
        # 实例变量
        super().__init__(name, age)
        self.school = school # public
        self.__score = 0 # private
        # 构造函数中访问类变量
        self.__class__.total += 1

    # 实例方法
    def to_str(self):
        # super(Student, self).to_str()
        super().to_str()
        print(self.name, self.age, self.school, self.__score)

    # 实例变量建议私有，通过提供方法来修改值
    def marking(self, score):
        self.__p_method()
        self.print_total()
        if score < 0:
            return 'negative score!!!'
        self.__score = score

    # 私有方法
    def __p_method(self):
        print('private method', self.__hash__())

    # 类方法
    @classmethod
    def print_total(cls):
        # 实例方法中访问类变量
        print('total:', cls.total)

    # 静态方法
    @staticmethod
    def print_total2():
        print('total:', Student.total)
