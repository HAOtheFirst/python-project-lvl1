from brain_games.cli import welcome_user
import random
import prompt


def game_progression():
    name = welcome_user()
    print('What number is missing in the progression?')

    i = 0

    while i < 3:
        value = random.randint(1, 10)
        d = random.randint(1, 10)
        len_progression = random.randint(5, 10)
        progression = []
        for a in range(0, len_progression):
            nam = value + (a * d)
            progression.append(nam)

        element = random.randint(0, len_progression - 1)
        correct_answer = progression[element]
        progression.remove(progression[element])
        progression.insert(element, '..')

        progression_string = ''

        for char in progression:
            progression_string += f'{char} '

        print(f'Question: {progression_string}')
        answer = prompt.real('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was "
                         f"'{correct_answer}'.'\n Let's try again, {name}!")

    if i == 3:
        print(f'Congratulations, {name}!')
