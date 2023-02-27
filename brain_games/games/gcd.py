from random import randint
import math


TASK = 'Find the greatest common divisor of given numbers.'
LOWER_LIMIT = 1
UPPER_LIMIT = 10


def get_game_data():
    first_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    second_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f"{first_number} {second_number}"
    answer = math.gcd(first_number, second_number)
    return question, str(answer)
