
def curve_pre():
    a = 25

    def curve(x):
        return a*x*x

    # 返回的不仅仅是函数，还包括环境变量a
    return curve


a = 10
f = curve_pre()
print(f.__closure__[0].cell_contents)
print(f(2))
