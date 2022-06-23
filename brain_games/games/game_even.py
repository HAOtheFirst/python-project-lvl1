#!/usr/bin/env python
from brain_games.cli import welcome_user, start_game, is_done
import random
import prompt


def game_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start_game(even, name, 2)


def even(name):
    number = random.randint(1, 100)
    print(f'Question: {number}')

    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    answer = prompt.string('Your answer: ')

    if is_done(answer, correct_answer, name) is True:
        return True
    else:
        return False
