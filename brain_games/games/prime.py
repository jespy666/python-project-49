from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_game():
    question = randint(1, 100)
    answer = is_prime(question)
    return question, answer


def is_prime(number):
    counter = 0
    i = 1
    while i <= number:
        if number % i == 0:
            counter += 1
        i += 1
    if counter == 2:
        return 'yes'
    return 'no'
