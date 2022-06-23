from brain_games.cli import welcome_user, start_game, is_done
import random
import prompt


def game_progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    start_game(progression, name, 2)


def progression(name):
    value = random.randint(1, 10)
    d = random.randint(1, 10)
    len_progression = random.randint(5, 10)
    progression_list = []
    for a in range(0, len_progression):
        nam = value + (a * d)
        progression_list.append(nam)

    element = random.randint(0, len_progression - 1)
    correct_answer = progression_list[element]
    progression_list.remove(progression_list[element])
    progression_list.insert(element, '..')

    progression_string = ''

    for char in progression_list:
        progression_string += f'{char} '

    print(f'Question: {progression_string}')
    answer = prompt.real('Your answer: ')

    if is_done(answer, correct_answer, name) is True:
        return True
    else:
        return False
