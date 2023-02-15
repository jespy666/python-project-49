from brain_games.cli import welcome_user
import prompt


def run_game(name_of_game):
    print('Welcome to the Brain Games!')
    player_name = welcome_user()
    print(name_of_game.EXERCISE)
    for i in range(3):
        question, answer = name_of_game.start_game()
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
