#!/usr/bin/env python
from brain_games.cli import welcome_user
import random
import prompt


def game_even():

    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0
    while i < 3:
        number = random.randint(1, 100)

        print(f'Question: {number}')

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        answer = prompt.string('Your answer: ')

        if (answer == correct_answer and number % 2 == 0) \
                or (answer == correct_answer and number % 2 != 0):
            print('Correct!')
            i += 1
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was "
                         f"'{correct_answer}'.'\n Let's try again, {name}!")

    if i == 3:
        print(f'Congratulations, {name}!')