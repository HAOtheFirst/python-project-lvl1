from brain_games.cli import welcome_user, is_done, start_game
import random
import prompt


def game_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    start_game(calc, name, 2)


def calc(name):
    operator = "+-*"
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    operation = random.choice(operator)

    print(f'Question: {number_one} {operation} {number_two}')

    correct_answer = eval(f'{number_one} {operation} {number_two}')

    answer = prompt.real('Your answer: ')

    if is_done(answer, correct_answer, name) is True:
        return True
    else:
        return False
