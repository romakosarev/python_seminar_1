# 1) Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

week_day = int(input('Введите номер дня недели: '))
if week_day in range(1, 7+1):
    if week_day in range(6,7+1):
        print('Да, это выходной')
    else:
        print('Нет, это будний день')
else:
    print('Неккоректный ввод ,Введите значение от 1 до 7')



# 2) Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(0, 1+1):
    for y in range(0, 1+1):
        for z in range(0, 1+1):
            print(x, y, z, end=' : ')
            print(not (x or y or z) == ((not x) and (not y) and (not z)))


# 3) Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = float(input('Введите x: '))
y = float(input('Введите y: '))
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)


# 4) Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input('Введите номер четверти: '))
if num in range(1, 4+1):
    if num == 1:
        print('x>0 y>0')
    elif num == 2:
        print('x<0  y>0')
    elif num == 3:
        print('x<0 y<0')
    else:
        print('x>0 y<0')
else:
    print('Неккоректное значение, введите значение от 1 до 4')




# 5) Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


x1 = float(input('Введите координаты x1: '))
y1 = float(input('Введите координаты y1: '))
x2 = float(input('Введите координаты x2: '))
y2 = float(input('Введите координаты y2: '))
bc = x1 - x2
ac = y2 - y1
print((ac ** 2 + bc ** 2) ** 0.5)

