#!/usr/bin/env python
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_done(answer, correct_answer, name):
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was "
              f"'{correct_answer}'.'\n Let's try again, {name}!")
        return False


def get_prime(max_range):
    prime_list = []
    for i in range(1, max_range):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list, max_range


if __name__ == "__main__":
    welcome_user()
