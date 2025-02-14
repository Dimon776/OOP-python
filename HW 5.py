import random

class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "???"


class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        return f"Moving at {self.speed} km/h"


class CyborgAnimal(Animal, Vehicle):
    def __init__(self, species, speed, power):
        Animal.__init__(self, species)
        Vehicle.__init__(self, speed)
        self.power = power

    def show_info(self):
        return f"{self.species} with speed {self.speed} km/h and power {self.power}."


cyborg = CyborgAnimal("Wolf", 50, "Laser Eyes")
print(cyborg.show_info())
print(cyborg.move())
print(cyborg.make_sound())



class Cipher:
    def __init__(self, *numbers):
        self.__numbers = numbers
        self.__result = self.__encrypt()

    def __encrypt(self):
        operation = random.choice(["+", "-", "*", "/"])
        if operation == "+":
            return sum(self.__numbers)
        elif operation == "-":
            return self.__numbers[0] - sum(self.__numbers[1:])
        elif operation == "*":
            result = 1
            for num in self.__numbers:
                result *= num
            return result
        elif operation == "/":
            result = self.__numbers[0]
            for num in self.__numbers[1:]:
                result /= num if num != 0 else 1
            return result

    def __str__(self):
        return f"Encrypted result: {self.__result}"


cipher = Cipher(10, 5, 2)
print(cipher)