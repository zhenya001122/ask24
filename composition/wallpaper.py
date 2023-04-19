"""Модуль для расчета рабочей площади помещения
и количества рулонов обоев"""

class WinDoor:
    """Класс окна двери
    Конструктор принимает длину и ширину"""
    def __init__(self, x, y):
        self.square = x * y

class Wallpaper:
    """Класс обои
    Конструктор принимает длину и ширину"""
    def __init__(self, x, y):
        self.square = x * y

class Room:
    """Класс комната
    Конструктор принимает ширину, длину, высоту.
    Обявляется список объектов проемов (окон и дверей)"""
    def __init__(self, x, y, z):
        self.width = x
        self.lenght = y
        self.height = z
        self.wd = []

    def squareRoom(self):
        """Метод для вычисления полной площади стен"""
        square = 2 * self.height * (self.width + self.lenght)
        return square

    def addWD(self, w, h):
        """Метод для добавления в список обектов проемов"""
        self.wd.append(WinDoor(w, h))

    def addWallpaper(self, w, h):
        """Метод для расчета площади катушки обоев и
        количества рулонов для оклейки рабочей площади стен"""
        self.square = w * h
        amount = Room.workSurface(self) / self.square  # количество рулонов
        return amount

    def workSurface(self):
        """Метод для расчета площади оклеиваемой поверхности"""
        new_square = Room.squareRoom(self)
        for i in self.wd:
            new_square -= i.square #площадь оклеиваемой поверхности
        return new_square

