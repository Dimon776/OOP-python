
class IterableGenerator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return (x for x in range(self.start, self.stop))

iterable = IterableGenerator(1, 5)
for num in iterable:
    print(num)

import operator

def safe_calculator(func):
    def wrapper(expression):
        allowed_operators = {"+", "-", "*", "/", "**", "%"}

        for char in expression:
            if not (char.isdigit() or char.isspace() or char in allowed_operators):
                return "Error: Invalid character in expression"

        try:
            result = func(expression)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception as e:
            return f"Error: {str(e)}"

    return wrapper


@safe_calculator
def calculate(expression):
    return eval(expression)



print(calculate("10 + 5"))
print(calculate("10 / 0"))
print(calculate("10 + abc"))
