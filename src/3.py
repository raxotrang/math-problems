from random import randint

def get_random_math_problem():
    operands = [randint(0, 10), randint(0, 10)]
    operator = ["+", "-", "*", "/"][randint(0, 3)]
    answer = str(eval("".join([str(operand) for operand in operands]))) + operator + str(operands[-1])
    return answer