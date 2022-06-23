#!/usr/bin/env python
from ..cli import welcome_user, get_prime_list, is_done, start_game
import random
import prompt
import time


def game_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    start_game(prime, name, 2)


def prime(name):
    prime_list, max_range = get_prime_list(100000)
    number = random.randint(1, max_range)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')

    if number in prime_list:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    if is_done(answer, correct_answer, name) is True:
        return True
    else:
        return False
