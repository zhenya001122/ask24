class Person:
    def __init__(self, first_name, last_name, qualification = 1):
        self.first_name = first_name
        self.last_name = last_name
        self.qualification = qualification

    def __del__(self):
        print("До свидания, мистер", self.first_name, self.last_name)

    def info(self):
        info_person = f"{self.first_name}, {self.last_name}, {self.qualification}"
        return info_person

person1 = Person("Vasya", "Ivanov", 6)
person2 = Person("Petya", "Petrov", 4)
person3 = Person("Kolya", "Sidorov", 5)

print(f"{person1.info()}\n{person2.info()}\n{person3.info()}")
del person2

s = input()
