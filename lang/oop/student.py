
class Student():
    name = ''
    age = 0

    def print_file(self):
        print(self.name, self.age)


student = Student()
student.name = 'Lily'
student.age = 24
student.print_file()