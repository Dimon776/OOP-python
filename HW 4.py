# import random
#
# class Human:
#     def __init__(self, name="Human", job=None, home=None, car=None, friend=None):
#         self.name = name
#         self.money = 100
#         self.gladness = 50
#         self.satiety = 50
#         self.job = job
#         self.car = car
#         self.home = home
#         self.friend = friend
#
#     def get_home(self):
#         self.home = House()
#
#     def get_car(self):
#         self.car = Auto(brands_of_car)
#
#     def get_job(self):
#         if self.car.drive():
#             pass
#         else:
#             self.to_repair()
#             return
#         self.job = Job(job_list)
#
#     def get_friend(self):
#         self.friend = Friend()
#
#     def eat(self):
#         if self.home.food <= 0:
#             self.shopping("food")
#         else:
#             if self.satiety >= 100:
#                 self.satiety = 100
#                 return
#             self.satiety += 5
#             self.home.food -= 5
#
#     def work(self):
#         if self.car.drive():
#             pass
#         else:
#             if self.car.fuel < 20:
#                 self.shopping("fuel")
#                 return
#             else:
#                 self.to_repair()
#                 return
#         self.money += self.job.salary
#         self.gladness -= self.job.gladness_less
#         self.satiety -= 4
#
#     def shopping(self, manage):
#         if self.car.drive():
#             pass
#         else:
#             if self.car.fuel < 20:
#                 manage = "fuel"
#             else:
#                 self.to_repair()
#                 return
#         if manage == "fuel":
#             self.money -= 100
#             self.car.fuel += 100
#         elif manage == "food":
#             self.money -= 50
#             self.home.food += 50
#         elif manage == "delicacies":
#             self.gladness += 10
#             self.satiety += 2
#             self.money -= 15
#
#     def chill(self):
#         self.gladness += 10
#         self.home.mess += 5
#
#     def clean_home(self):
#         self.gladness -= 5
#         self.home.mess = 0
#
#     def to_repair(self):
#         self.car.strength += 100
#         self.money -= 50
#
#     def invite_friend(self):
#         if self.friend:
#             self.friend.visit(self)
#
#     def days_indexes(self, day):
#         print(f"{'Today the ' + str(day) + ' of ' + self.name + "'s life":=^50}")
#         print(f"Money – {self.money}")
#         print(f"Satiety – {self.satiety}")
#         print(f"Gladness – {self.gladness}")
#         print(f"Food – {self.home.food}")
#         print(f"Mess – {self.home.mess}")
#         print(f"{self.car.brand} car: Fuel – {self.car.fuel}, Strength – {self.car.strength}")
#
#     def is_alive(self):
#         if self.gladness < 0:
#             print("Depression…")
#             return False
#         if self.satiety < 0:
#             print("Dead…")
#             return False
#         if self.money < -500:
#             print("Bankrupt…")
#             return False
#         return True
#
#     def live(self, day):
#         if not self.is_alive():
#             return False
#         if self.home is None:
#             self.get_home()
#         if self.car is None:
#             self.get_car()
#         if self.job is None:
#             self.get_job()
#         if self.friend is None:
#             self.get_friend()
#         self.days_indexes(day)
#         dice = random.randint(1, 5)
#         if self.satiety < 20:
#             self.eat()
#         elif self.gladness < 20:
#             if self.home.mess > 15:
#                 self.clean_home()
#             else:
#                 self.chill()
#         elif self.money < 0:
#             self.work()
#         elif self.car.strength < 15:
#             self.to_repair()
#         elif dice == 1:
#             self.chill()
#         elif dice == 2:
#             self.work()
#         elif dice == 3:
#             self.clean_home()
#         elif dice == 4:
#             self.shopping("delicacies")
#         elif dice == 5:
#             self.invite_friend()
#
# class Friend:
#     def visit(self, human):
#         event = random.choice(["gift", "walk", "chat"])
#         if event == "gift":
#             human.money += 20
#             print(f"Friend brought a gift! +20 money")
#         elif event == "walk":
#             human.gladness += 15
#             human.money -= 10
#             print(f"Went on a walk with friend! +15 gladness, -10 money")
#         elif event == "chat":
#             human.gladness += 10
#             print(f"Had a great chat with friend! +10 gladness")
#
# brands_of_car = {
#     "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
#     "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
#     "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
#     "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
# }
#
# class Auto:
#     def __init__(self, brand_list):
#         self.brand = random.choice(list(brand_list))
#         self.fuel = brand_list[self.brand]["fuel"]
#         self.strength = brand_list[self.brand]["strength"]
#         self.consumption = brand_list[self.brand]["consumption"]
#
#     def drive(self):
#         if self.strength > 0 and self.fuel >= self.consumption:
#             self.fuel -= self.consumption
#             self.strength -= 1
#             return True
#         else:
#             return False
#
# class House:
#     def __init__(self):
#         self.mess = 0
#         self.food = 0
#
# job_list = {
#     "Java developer": {"salary": 50, "gladness_less": 10},
#     "Python developer": {"salary": 40, "gladness_less": 3},
#     "C++ developer": {"salary": 45, "gladness_less": 25},
#     "Rust developer": {"salary": 70, "gladness_less": 1},
# }
#
# class Job:
#     def __init__(self, job_list):
#         self.job = random.choice(list(job_list))
#         self.salary = job_list[self.job]["salary"]
#         self.gladness_less = job_list[self.job]["gladness_less"]
#
# nick = Human(name="Nick")
# for day in range(1, 800):
#     if not nick.live(day):
#         break



import random

class Student:
    def __init__(self, name):
        self.name = name
        self.knowledge = 0
        self.mood = 50

    def study(self, teacher):
        if self.mood > 10:
            teacher.teach(self)
        else:
            print(f"{self.name} слишком устал, чтобы учиться.")

    def relax(self):
        self.mood += 15
        print(f"{self.name} отдохнул и теперь его настроение {self.mood}.")

    def show_status(self):
        print(f"Ученик: {self.name}, Знания: {self.knowledge}, Настроение: {self.mood}")

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self, student):
        student.knowledge += 10
        student.mood -= 10
        print(f"{self.name} научил {student.name} предмету {self.subject}. Знания: {student.knowledge}, Настроение: {student.mood}")

teacher = Teacher("Иван Иванович", "Математика")
students = [Student("Петя"), Student("Маша"), Student("Саша")]

for day in range(1, 6):
    print(f"\nДень {day}")
    for student in students:
        if random.choice([True, False]):
            student.study(teacher)
        else:
            student.relax()
        student.show_status()