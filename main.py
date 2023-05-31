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

# 4.1
a=float(input('Первое число: '))
b=float(input('Второе число: '))
print(a if a > b else b)
print(a if a < b else b)

# 2.14
a = int(input('введите катет (a): '))
b = int(input('введите катет (b): '))
c = math.sqrt(a ** 2 + b ** 2)
print("гипотенузу (с): ", c)

# 2.15
R = int(input("внешний радиус (R): "))
r = int(input("внутренний радиус (r): "))
S = 3.14 * (R ** 2 - r ** 2)
print("площадь (S): ", S)

# 2.16
a = int(input("первый катет (a): "))
b = int(input("второй катет (b): "))
c = math.sqrt(a ** 2 + b ** 2)
p = a+b+c
print ("Периметр треугольника равен (p): ", p)

# 2.17
a = int(input("Длина большего основания (a):"))
b = int(input("Длина меньшего основания (b):"))
h = int(input("Высота (h):"))
P = a + b + 2 * math.sqrt(h ** 2 + ((a - b) ** 2) / 4)
print("Периметр (P):", P)

# 2.18
x = int(input("введите (x):"))
y = int(input("введите (y):"))
z = (x + (2 + y/x ** 2)) / (y + (1 / math.sqrt(x ** 2 + 10)))
print("результат (z):", z)

x = int(input("введите (x):"))
y = int(input("введите (y):"))
q = 7.25 * math.sqrt(x) - math.fabs(y)
print("результат (q):", q)

# 2.19
a= int(input("введите a : "))
b= int(input("введите b : "))
x = (2/(a**2+25)-b)/(math.sqrt(b) + (a+b)/2)
y = (math.fabs(a) + 2*math.sin(b))/5.5*a
print(x)
print(y)

# 2.20
e= int(input("введите e : "))
f= int(input("введите f : "))
g= int(input("введите g : "))
h= int(input("введите h : "))
a=math.sqrt(math.fabs(e-(3/f)**3)+g)
b= math.sin(e)+math.cos(h)**2
c=(33*g/(e*f-3))
print (a)
print (b)
print (c)

# 2.21
e= int(input("введите e : "))
f= int(input("введите f : "))
g= int(input("введите g : "))
h= int(input("введите h : "))
a = (e+(f/2))/3
b = math.fabs(h ** 2 - g)
c = math.sqrt((g-h)**2)-3*math.sin(e)
print(a)
print(b)
print(c)

# 11.2
a= int(input("введите a : "))
b= int(input("введите b : "))
c= int(input("введите c : "))
d= int(input("введите d : "))
f= int(input("введите f : "))
e= int(input("введите e : "))
g= int(input("введите g : "))
h= int(input("введите h : "))
j= int(input("введите j : "))
k= int(input("введите k : "))
nech = [a, b, c, d, f,e,g,h,j,k]
for i in nech:
    print(i, end=' ')

# 11.1
x=[37,0,50,46,34,46,0,13]
for i in x:
    print(i, end=' ')

# 11.4
a = ["#" for i in range(0,20)]

# 12.1
name = input("Введите имя: ")
family = input("Введите фамилию: ")
result = name + " " + family
print(result)

# 12.17
s = input("введите слово:")
print(s[1] + s[3])

# 12.18
s = input("введите слово():")
print(s[2] + s[-1])

# 12.19
s = input("введите слово:")
print(s[1] + s[2] + s[3])


