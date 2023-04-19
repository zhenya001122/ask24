from random import randint


class Voin:

    def __init__(self, health, name):
        self.health = health
        self.name = name

    def strike(self, name_attack):
        if self.health > 0:
            self.health -= 20
            print(f"Атаковал {name_attack}. У {self.name} осталось здоровья - {self.health}")

warrior1 = Voin(100, "unit1")
warrior2 = Voin(100,  "unit2")
warriors = [warrior1, warrior2]

count = 0
while count < 10:
    rnd = randint(1, 2)
    if rnd == 1:
        warrior1.strike(warrior2.name)
        if warrior1.health == 0:
            print(f'{warrior1.name} погиб')
            break
    elif rnd == 2:
        warrior2.strike(warrior1.name)
        if warrior2.health == 0:
            print(f'{warrior2.name} погиб')
            break
    count += 1
