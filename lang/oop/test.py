from student import Student

student = Student('Lily', 24)
student.to_str()
print(student.name)
print(student.age)
print(Student.total)

print(student.__dict__)
