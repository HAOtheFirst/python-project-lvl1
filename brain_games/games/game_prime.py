#!/usr/bin/env python
from ..cli import welcome_user
import random
import prompt


# def is_even(value1, value2=2):
#     return True if value1 % value2 == 0 else False
#
# list_prime = [num for num in range(2, random_num // 2)\
#                   if not is_even(random_num, num)]
#     print(list_prime, random_num)

def game_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    max_range = 500
    prime_list = []

    for i in range(1, max_range):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)

    i = 0

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
