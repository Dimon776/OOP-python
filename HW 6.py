result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("Первое число меньше второго")
        if b > 100:
            raise IndexError("Второе число больше 100")
        return a / b
    except ZeroDivisionError:
        print(f"Ошибка: деление на ноль ({a} / {b})")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except IndexError as e:
        print(f"Ошибка: {e}")
    except TypeError:
        print(f"Ошибка: некорректный тип данных ({a}, {b})")

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(key, value)
        if res is not None:
            result.append(res)
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

print("Результат:", result)
