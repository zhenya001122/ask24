from random import randint
"""В некой игре-стратегии есть солдаты и герои. У всех есть свойство,
 содержащее уникальный номер объекта, и свойство, в котором хранится 
 принадлежность команде. У солдат есть метод "иду за героем", который
  в качестве аргумента принимает объект типа "герой". У героев есть метод
   увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды. 
В цикле генерируются объекты-солдаты. Их принадлежность команде определяется 
случайно. Солдаты разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран.
 У героя, принадлежащего команде с более длинным списком, поднимается уровень.
Отправьте одного из солдат первого героя следовать за ним. Выведите на экран 
идентификационные номера этих двух юнитов."""

class Party:
    __count = 1
    def __init__(self, number_group):
        self.number_group = number_group
        self.number_personal = Party.__count
        Party.__count += 1

class Soldier(Party):
    def follow_the_hero(self, number_hero):
        print(f'Иду за героем {number_hero}')

class Hero(Party):
    def __init__(self, number_group):
        Party.__init__(self, number_group)
        self.level = 0

    def increase_level(self): # увеличивает уровень героя
        self.level += 1

hero1 = Hero(1)
hero2 = Hero(2)
team1 = [] #команда 1
team2 = [] #команда 2

for i in range(20): # рандомно создает группы солдат
    num_group = randint(1, 2)
    if num_group == 1:
        team1.append(Soldier(num_group))
    elif num_group == 2:
        team2.append(Soldier(num_group))

print(f"Численность команды 1 = {len(team1)}\n"
      f"Численность команды 2 = {len(team2)}")

if len(team1) > len(team2):
    hero1.increase_level()
elif len(team1) < len(team2):
    hero2.increase_level()
else:
    print("Уровни героев равны")

print(f"Уровень первого героя - {hero1.level}\n"
      f"Уровень второго героя - {hero2.level}")

team1[0].follow_the_hero(hero1.number_personal) #отправляем солдата за первым героем
print(f"Номер солдата - {team1[0].number_personal}\n"
      f"Номер героя - {hero1.number_personal}")