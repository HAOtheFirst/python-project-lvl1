#!/usr/bin/env python
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start_game(func, text, game_count):
    back_func = func(text)
    if game_count == 0 and back_func is True:
        return print(f'Congratulations, {text}!')
    elif back_func is True:
        return start_game(func, text, game_count - 1)
    else:
        return


def is_done(answer, correct_answer, name):
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was "
              f"'{correct_answer}'.'\n Let's try again, {name}!")
        return False


# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False


def get_prime_list(max_range):
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
