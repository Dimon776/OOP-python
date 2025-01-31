import math
import random


def greet_user():
    name = input("Введіть ваше ім'я: ")
    age = input("Введіть ваш вік: ")
    print(f"Привіт {name}, тобі {age}!")


def check_age():
    age = int(input("Введіть ваш вік: "))
    if age >= 18:
        print("Вхід дозволено!")
    else:
        print("Вхід заборонено!")


def guess_number():
    number = random.randint(1, 10)
    attempts = 3

    for _ in range(attempts):
        guess = int(input("Вгадайте число від 1 до 10: "))
        if guess == number:
            print("Вітаю, ви вгадали!")
            return
        elif guess > number:
            print("Менше")
        else:
            print("Більше")

    print(f"Ви програли! Загадане число було {number}")


def print_range():
    start = int(input("Введіть початкове число: "))
    end = int(input("Введіть кінцеве число: "))
    for i in range(start, end + 1):
        print(i, end=' ')
    print()


def reverse_even_numbers():
    n = int(input("Введіть число n: "))
    for i in range(n, 0, -1):
        if i % 2 == 0:
            print(i, end=' ')
    print()


def factorial():
    n = int(input("Введіть число для обчислення факторіалу: "))
    print(f"Факторіал {n} = {math.factorial(n)}")


def grade_student():
    score = int(input("Введіть кількість отриманих балів: "))
    if 0 <= score <= 49:
        print("Незадовільно")
    elif 50 <= score <= 69:
        print("Задовільно")
    elif 70 <= score <= 89:
        print("Добре")
    elif 90 <= score <= 100:
        print("Відмінно")
    else:
        print("Некоректна кількість балів")


def calculator():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    operation = input("Введіть операцію (+, -, *, /): ")

    if operation == '+':
        print(f"Результат: {a + b}")
    elif operation == '-':
        print(f"Результат: {a - b}")
    elif operation == '*':
        print(f"Результат: {a * b}")
    elif operation == '/':
        if b == 0:
            print("Ділення на нуль")
        else:
            print(f"Результат: {a / b}")
    else:
        print("Некоректна операція")