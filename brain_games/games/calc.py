from random import randint, choice


TASK = 'What is the result of the expression?'
LOWER_LIMIT = 1
UPPER_LIMIT = 10
SIGNS = ['*', '+', '-']


def calculate(number_1, number_2, sign):
    if sign == '*':
        return number_1 * number_2
    elif sign == '+':
        return number_1 + number_2
    elif sign == '-':
        return number_1 - number_2


def get_game_data():
    first_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    second_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    sign = choice(SIGNS)
    question = f'{first_number} {sign} {second_number}'
    answer = calculate(first_number, second_number, sign)
    return question, str(answer)
