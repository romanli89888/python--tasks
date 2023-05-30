import math
# 2.1
def y(x):
    return 17 * x ** 2 - 6 * x + 13
def y2(a):
    return 3 * a ** 2 + 5 * a - 21

print(y(3))
print(y2(2))

# 2.2
def y3(a):
    return a ** 2 + 10 / math.sqrt(a ** 2 + 1)

print(y3(5))

# 2.3
def y4(a):
    return math.sqrt(2 * a + math.sin(math.fabs(3 * a))) / 3.56

print(y4(4))


def y5(x):
    return math.sin(3.2 + (math.sqrt(1 + x))) / math.fabs(5 * x)

print(y5(5))

# 2.4

a = int(input('введите сторону квадрата (a): '))
P = 4 * a
print("периметр квадрата P: ", P)

# 2.5

r = int(input('введите радиус окружности (r): '))
D = 2 * r
print("диаметр окружности D: ", D)




