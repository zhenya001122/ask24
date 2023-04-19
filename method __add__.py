class Method:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return other+self.x
    def __str__(self):
        return str(self.x)

a = Method(2)
b = 4
c = a + b
print(c)
