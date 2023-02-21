from random import randint


TASK = 'What number is missing in the progression?'
LOWER_START_LIMIT = 1
UPPER_START_LIMIT = 10
MIN_MISSING_MEMBER = 0
MAX_MISSING_MEMBER = 9
MIN_COMMON_DIFFERENCE = 2
MAX_COMMON_DIFFERENCE = 5
PROGRESSION_LENGTH = 10


def get_progression():
    common_difference = randint(MIN_COMMON_DIFFERENCE, MAX_COMMON_DIFFERENCE)
    i = randint(LOWER_START_LIMIT, UPPER_START_LIMIT)
    progression = []
    while len(progression) < PROGRESSION_LENGTH:
        progression.append(i)
        i += common_difference
    return progression


def get_game_data():
    progression = get_progression()
    missing_member = randint(MIN_MISSING_MEMBER, MAX_MISSING_MEMBER)
    answer = progression[missing_member]
    progression[progression.index(answer)] = '..'
    question = ' '.join(map(str, progression))
    return question, str(answer)
