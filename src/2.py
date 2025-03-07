import random
def get_random_math_problem():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    operation = ['+', '-', '*', '/']
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    op = random.choice(operation)
    if op == '+':
        return f'{num1} + {num2}'
    elif op == '-':
        return f'{num1} - {num2}'
    elif op == '*':
        return f'{num1} * {num2}'
    else:
        return f'{num1} / {num2}'