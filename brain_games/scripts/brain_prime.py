#!/usr/bin/env python3
from brain_games.games import brain_prime
from brain_games import game_engine


def main():
    game_engine.run_game(brain_prime)


if __name__ == '__main__':
    main()
