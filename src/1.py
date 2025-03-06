import random

def get_random_math_problem():
    numbers = [1, 2, 3, 4, 5]
    number1 = random.choice(numbers)
    numbers.remove(number1)
    number2 = random.choice(numbers)
    problem = f"{number1} + {number2} = "
    answer = number1 + number2
    return problem, answer
