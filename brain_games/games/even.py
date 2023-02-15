from random import randint


EXERCISE = 'Answer "yes" if the number is even, otherwise answer "no".'


def start_game():
    question = randint(1, 100)
    answer = is_even(question)
    return question, answer


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    elif number % 2 != 0:
        return 'no'
