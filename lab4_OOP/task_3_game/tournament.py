# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *
import sys


def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print('Вышел', dragon._color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = input('Ответ:')
            if answer == 'end':
                sys.exit()
            try:
                answer = int(answer)
                if dragon.check_answer(answer):
                    hero.attack(dragon)
                    hero._experience+=5
                    print('Верно! \n** дракон кричит от боли **')
                    print ('Здоровье дракона: ', dragon.get_health())
                else:
                    dragon.attack(hero)
                    hero._experience-=1
                    print('Ошибка! \n** вам нанесён удар... **')
                    print ('Твое здоровье: ', hero.get_health())
            except ValueError:
                print ('Невозможное значение, вот вам другое задание.')
        if dragon.is_alive():
            break
        print('Дракон', dragon._color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print ('Вы можете выйти из игра во время ответов, написав \'end\' ')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 3
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 3)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
