from brain_games.cli import welcome_user, is_done
import random
import prompt


def game_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    operator = "+-*"
    i = 0

    while i < 3:
        number_one = random.randint(1, 100)
        number_two = random.randint(1, 100)
        operation = random.choice(operator)

        print(f'Question: {number_one} {operation} {number_two}')

        correct_answer = eval(f'{number_one} {operation} {number_two}')

        answer = prompt.real('Your answer: ')

        if is_done(answer, correct_answer, name) is True:
            i += 1

    if i == 3:
        print(f'Congratulations, {name}!')
