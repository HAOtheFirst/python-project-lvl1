#!/usr/bin/env python
from ..cli import welcome_user, get_prime
import random
import prompt


def game_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    get_prime(500)

    i = 0

    prime_list, max_range = get_prime(500)
    while i < 3:
        number = random.randint(1, max_range)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        if number in prime_list:
            current_answer = 'yes'
        else:
            current_answer = 'no'

        if answer == current_answer:
            print('Correct!')
            i += 1
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was "
                         f"'{current_answer}'.'\n Let's try again, {name}!")

    if i == 3:
        print(f'Congratulations, {name}!')
