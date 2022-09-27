# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт 
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Enter x coordinates: '))
y = int(input('Enter y coordinates: '))
if x > 0 and y > 0:
    print('It is first quarter')
elif x > 0 and y < 0:
    print('It is second quarter')
elif x < 0 and y < 0:
    print('It is third quarter')
else:
    print('It is fourth quarter')