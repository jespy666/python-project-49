from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_LIMIT = 1
UPPER_LIMIT = 10


def is_prime(number):
    counter = 0
    i = 1
    while i <= number:
        if number % i == 0:
            counter += 1
        i += 1
    if counter == 2:
        return True
    return False


def get_game_data():
    question = randint(LOWER_LIMIT, UPPER_LIMIT)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
