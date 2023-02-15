#!/usr/bin/env python3
from brain_games.games import even
from brain_games import game_engine


def main():
    game_engine.run_game(even)


if __name__ == '__main__':
    main()
