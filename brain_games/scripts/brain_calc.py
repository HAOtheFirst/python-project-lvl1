#!/usr/bin/env python
from brain_games.games.game_calc import game_calc
from ..cli import welcome_user


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    game_calc(name)


if __name__ == "__main__":
    main()
