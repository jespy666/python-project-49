from random import randint, choice


TASK = 'What is the result of the expression?'


def start_game():
    number_1 = randint(1, 10)
    number_2 = randint(1, 10)
    sign = choice(['*', '+', '-'])
    question = f'{number_1} {sign} {number_2}'
    answer = calculate(number_1, number_2, sign)
    return question, str(answer)


def calculate(number_1, number_2, sign):
    if sign == '*':
        return number_1 * number_2
    elif sign == '+':
        return number_1 + number_2
    elif sign == '-':
        return number_1 - number_2
