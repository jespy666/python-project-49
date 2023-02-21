from brain_games.cli import welcome_user
import prompt


ROUNDS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    player_name = welcome_user()
    print(game.TASK)
    for i in range(ROUNDS):
        question, answer = game.get_game_data()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        elif user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {player_name}!")
            break
    else:
        print(f'Congratulations, {player_name}!')
