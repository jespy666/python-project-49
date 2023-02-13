from random import randint
from brain_games.cli import welcome_user


def brain_even():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        question = randint(0, 100)
        user_input = input(f'Question: {question}\n')
        answer = ''
        if question % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        if user_input != answer:
            print(f"'{user_input}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            break
        else:
            print(f'Your answer: {user_input}\nCorrect!')
    else:
        print(f'Congratulations, {name}!')

