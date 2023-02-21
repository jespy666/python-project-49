from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_LIMIT = 1
UPPER_LIMIT = 10


def is_even(number):
    return number % 2 == 0


def get_game_data():
    question = randint(LOWER_LIMIT, UPPER_LIMIT)
    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
