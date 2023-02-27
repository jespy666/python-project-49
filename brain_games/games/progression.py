from random import randint


TASK = 'What number is missing in the progression?'
LOWER_START_LIMIT = 1
UPPER_START_LIMIT = 10
MIN_MISSING_MEMBER = 0
MAX_MISSING_MEMBER = 9
MIN_COMMON_DIFFERENCE = 2
MAX_COMMON_DIFFERENCE = 5
PROGRESSION_LENGTH = 10


def get_progression(progression_length, first_member, common_difference):
    progression = []
    i = first_member
    while len(progression) <= progression_length:
        progression.append(i)
        i += common_difference
    return progression


def get_question(progression):
    question = ''
    for j in progression:
        question += str(j) + ' '
    return question[:-1]


def get_game_data():
    first_member = randint(LOWER_START_LIMIT, UPPER_START_LIMIT)
    common_difference = randint(MIN_COMMON_DIFFERENCE, MAX_COMMON_DIFFERENCE)
    progression = get_progression(PROGRESSION_LENGTH, first_member, common_difference)
    missing_member = randint(MIN_MISSING_MEMBER, MAX_MISSING_MEMBER)
    answer = progression[missing_member]
    progression[missing_member] = '..'
    question = get_question(progression)
    return question, str(answer)
