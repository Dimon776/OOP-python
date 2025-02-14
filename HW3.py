# import time
# import random
#
#
# class Cat:
#     def __init__(self, name):
#         self.name = name
#         self.energy = 100
#         self.hunger = 0
#         self.happiness = 100
#
#     def eat(self):
#         if self.hunger > 0:
#             print(f"{self.name} кушает... Мрр~")
#             self.hunger -= 20
#             self.energy += 10
#         else:
#             print(f"{self.name} не голоден.")
#         self.status()
#
#     def sleep(self):
#         print(f"{self.name} спит... Zzz...")
#         self.energy = 100
#         self.hunger += 10
#         time.sleep(1)
#         self.status()
#
#     def play(self):
#         if self.energy > 20:
#             print(f"{self.name} играет с клубком! 🧶")
#             self.energy -= 20
#             self.happiness += 20
#             self.hunger += 10
#         else:
#             print(f"{self.name} слишком устал, чтобы играть.")
#         self.status()
#
#     def purr(self):
#         print(f"{self.name} мурлычет... 💕 Мрррр~")
#         self.happiness += 10
#         self.status()
#
#     def status(self):
#         print(f"Статус {self.name}: Энергия {self.energy}, Голод {self.hunger}, Счастье {self.happiness}\n")
#
#     def live(self):
#         actions = [self.eat, self.sleep, self.play, self.purr]
#         for _ in range(5):
#             time.sleep(1)
#             random.choice(actions)()
#
# my_cat = Cat("Барсик")
# my_cat.live()


import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        if self.money >= 10:
            self.gladness += 5
            self.progress -= 0.1
            self.money -= 10
        else:
            print("Not enough money to chill")

    def to_work(self):
        print("Time to work")
        self.money += 20
        self.gladness -= 2

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.money < 0:
            print("Bankrupt…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:+^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        self.end_of_day()
        self.is_alive()


nick = Student(name="Nick")
kate = Student(name="Kate")
bohdan = Student(name="Bohdan")
for day in range(365):
    if not nick.alive:
        break
    nick.live(day)
    if not kate.alive:
        break
    kate.live(day)
    if not bohdan.alive:
        break
    bohdan.live(day)
