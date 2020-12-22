
def print_student(name, gender='男', age=18, college='武汉大学'):
    print('我叫' + name)
    print('我今年' + str(age) + '岁')
    print('我是' + gender + '生')
    print('我在' + college + '上学')


print_student('鸡小萌', '男', 18, '武汉大学')
print('~~~~~~~~~~~~~~~~~~~')
print_student('石敢当')
print('~~~~~~~~~~~~~~~~~~~')
print_student('喜小乐', '女', 16)
print('~~~~~~~~~~~~~~~~~~~')
print_student('猪八戒', college='华中科技大学', age=20)
