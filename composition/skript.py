from composition import wallpaper
from wallpaper import *


x = float(input('Введите ширину комнаты: '))
y = float(input('Введите длину комнаты: '))
z = float(input('Введите высоту комнаты: '))
r1 = Room(x, y, z)
number = int(input("Введите количество проемов: "))
for i in range(number):
    xw = float(input(f"Введите ширину проема {i+1}: "))
    yw = float(input(f"Введите высоту проема {i+1}: "))
    r1.addWD(xw, yw)
n = float(input("Длина рулона: "))
m = float(input("Ширина рулона: "))
print("Общая площадь стен составляет:", r1.squareRoom())
print("Рабочая площадь стен =", r1.workSurface())
print("Необходимое количество рулонов =", r1.addWallpaper(n, m))
