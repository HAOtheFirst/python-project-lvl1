from brain_games.cli import welcome_user
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

        if answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was "
                         f"'{correct_answer}'.'\n Let's try again, {name}!")

    if i == 3:
        print(f'Congratulations, {name}!')
