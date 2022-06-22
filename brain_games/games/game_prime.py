#!/usr/bin/env python
from ..cli import welcome_user, get_prime_list, is_done
import random
import prompt


def game_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    get_prime_list(500)

    i = 0

    prime_list, max_range = get_prime_list(500)
    while i < 3:
        number = random.randint(1, max_range)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        if number in prime_list:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if is_done(answer, correct_answer, name) is True:
            i += 1

    if i == 3:
        print(f'Congratulations, {name}!')
