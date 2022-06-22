from brain_games.cli import game_structure
import random


def game_calc(name):
    operator = "+-*"
    number_one = random.randint(1, 100)
    number_two = random.randint(1,  100)
    operation = random.choice(operator)
    correct_answer = eval(f'{number_one} {operation} {number_two}')
    question = f'Question: {number_one} {operation} {number_two}'

    game_structure(name, question, correct_answer, 3)
