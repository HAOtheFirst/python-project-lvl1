#!/usr/bin/env python
from ..cli import welcome_user
import random
import prompt


def game_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    i = 0

    while i < 3:
        first_num = random.randint(1, 1000)
        second_num = random.randint(1, 1000)
        print(f'Question: {first_num} {second_num}')
        answer = prompt.real('Your answer: ')

        first_reminder = max(first_num, second_num) % min(first_num, second_num)
        second_reminder = min(first_num, second_num) % first_reminder
        third_reminder = first_reminder % second_reminder

        while (first_reminder or second_reminder or third_reminder) != 0:
            if first_reminder == 0:
                divider = second_num
                break
            elif second_reminder == 0:
                divider = first_reminder
                break
            elif third_reminder == 0:
                divider = second_reminder
                break
            else:
                first_reminder = second_reminder
                second_reminder = third_reminder
                third_reminder = first_reminder % second_reminder
                continue

        if answer == divider:
            print('Correct!')
            i += 1

        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was "
                         f"'{divider}'.'\n Let's try again, {name}!")

    if i == 3:
        print(f'Congratulations, {name}!')
