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


if __name__ == "__main__":
    welcome_user()
