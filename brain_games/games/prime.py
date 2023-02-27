from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_LIMIT = 2
UPPER_LIMIT = 100


def is_prime(number):
    if number <= 1:
        return False
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1
    return True


def get_game_data():
    question = randint(LOWER_LIMIT, UPPER_LIMIT)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
