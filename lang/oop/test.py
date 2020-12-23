from student import Student

student = Student('Lily', 24)
print(student.name)
print(student.age)
student.to_str()

Student.print_total()

Student.print_total2()

print(student.__dict__)
# {'name': 'Lily', 'age': 24, '_Student__score': 0}
# print(student._Student__score)

result = student.marking(80)
if result:
    print(result)

student.to_str()

lucy = Student('Lucy', 24)
lee = Student('Lee', 25)
# 这里实际上是新创建一个实例变量，动态语言特性
lucy.__score = -1
# print(lucy.__score)
lucy.to_str()
