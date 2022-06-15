#!/usr/bin/env python
import random
import prompt


def game_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
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

        if answer == 'yes' and number % 2 == 0:
            print('Correct!')
            i += 1
        elif answer == 'no' and number % 2 != 0:
            print('Correct!')
            i += 1
        elif i == 2:
            print(f'Congratulations, {name}!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            i = 4
