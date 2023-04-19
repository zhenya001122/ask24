class Encaps:
    def __init__(self, x):
        self.__x = x

    def __method(self, b):
        c = self.__x + b
        return c

    def set_x(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

a = Encaps(2)
print(a._Encaps__x)
# print(a._Encaps__method(3))
a.set_x(8)
print(a.get_x())
