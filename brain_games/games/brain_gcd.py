from random import randint
import math


exercise = 'Find the greatest common divisor of given numbers.'


def start_game():
    number_1 = randint(1, 50)
    number_2 = randint(1, 50)
    answer = f"{number_1} {number_2}"
    question = math.gcd(number_1, number_2)
    return answer, str(question)
