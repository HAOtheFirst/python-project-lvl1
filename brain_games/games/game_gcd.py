#!/usr/bin/env python
from ..cli import welcome_user, start_game, is_done, find_gcd
import random
import prompt


def game_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    start_game(gcd, name, 2)


def gcd(name):
    first_num = random.randint(1, 1000)
    second_num = random.randint(1, 1000)
    print(f'Question: {first_num} {second_num}')
    answer = prompt.real('Your answer: ')

    correct_answer = find_gcd(first_num, second_num)

    if is_done(answer, correct_answer, name):
        return True
    else:
        return False
