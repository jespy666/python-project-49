from random import randint


TASK = 'What number is missing in the progression?'


def start_game():
    question, answer = choice_symbol()
    return question, str(answer)


def generate_subsequence():
    i = randint(1, 10)
    step = randint(2, 5)
    subsequence = []
    while len(subsequence) <= 10:
        subsequence.append(i)
        i += step
    return subsequence


def choice_symbol():
    sequence = generate_subsequence()
    hidden_symbol = randint(0, 9)
    answer = sequence[hidden_symbol]
    sequence[hidden_symbol] = '..'
    result = ''
    for j in sequence:
        result += str(j)
        result += ' '
    return result[:-1], answer
