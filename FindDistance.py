# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math
x1 = int(input('Enter x1 coordinates: '))
y1 = int(input('Enter y1 coordinates: '))
x2 = int(input('Enter x2 coordinates: '))
y2 = int(input('Enter y2 coordinates: '))
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(round(distance, 2))