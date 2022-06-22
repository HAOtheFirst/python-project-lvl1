#!/usr/bin/env python
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_structure(name, question, correct_answer, num_of_games):
    def is_done():
        if answer == correct_answer:
            print('Correct!')
            game_structure(name, question, correct_answer, num_of_games - 1)
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was "
                         f"'{correct_answer}'.'\n Let's try again, {name}!")

    if num_of_games == 0:
        print(f'Congratulations, {name}!')
    elif num_of_games > 0:
        print(question)
        answer = prompt.real('Your answer: ')
        is_done()


if __name__ == "__main__":
    welcome_user()
