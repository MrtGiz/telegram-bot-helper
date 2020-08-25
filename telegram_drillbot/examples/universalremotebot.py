#!/usr/bin/env python
# -*- coding: utf-8 -*-

# suppress some pylint warnings since this is a stub example
# pylint: disable=unused-argument
# pylint: disable=missing-docstring

import sys

from enum import Enum, auto
from collections import OrderedDict

from telegram_drillbot.drillbot.drillbot import DrillBot
from telegram_drillbot.drillbot.transition import MenuTransition, SaveTransition, NoTransition

from settings import TOKEN
from model import messages


def main():
    try:
        token = TOKEN
    except KeyError:
        sys.exit("Error: pass token as script argument")
    bot = UniversalRemoteBot(token)
    bot.start_bot()


class State(Enum):
    MENU = auto()
    PC = auto()
    PC_1 = auto()
    PC_2 = auto()
    PRINTER = auto()
    PRINTER_1 = auto()
    PRINTER_2 = auto()
    INTERNET = auto()
    INTERNET_1 = auto()
    INTERNET_2 = auto()
    PHONE = auto()
    PHONE_1 = auto()
    PHONE_2 = auto()
    NO_PROBLEM = auto()
    PROBLEM = auto()


class UniversalRemoteBot(DrillBot): # pylint: disable=too-few-public-methods
    def __init__(self, token):
        # pylint: disable=bad-whitespace
        # pylint: disable=bad-continuation
        transitions = {
            State.MENU: MenuTransition(title=messages['home']['text'],
                                       options=OrderedDict([
                                           ("ПК", State.PC),
                                           ("Принтер",  State.PRINTER),
                                           ("Интернет",  State.INTERNET),
                                           ("Телефон", State.PHONE),
                                       ])),

            # Проблемы с ПК
            State.PC: MenuTransition(title=messages['PC']['text'],
                                     options=OrderedDict([
                                         ("ПК проблема 1", State.PC_1),
                                         ("ПК проблема 2", State.PC_2),
                                     ])),

            State.PC_1: MenuTransition(title='Проблема с ПК 1\nВариант решения\nПомогло ли?',
                                       title_func=test_message,
                                       options=OrderedDict([
                                           ("Да", State.NO_PROBLEM),
                                           ("Нет", State.PROBLEM),
                                       ]),
                                       photo='https://images.app.goo.gl/tiWDtYXqCCEKDWWH9',
                                       caption=messages['instruction']['text']
                                       ),

            State.PC_2: MenuTransition(title='Проблема с ПК 2\nВариант решения\nПомогло ли?',
                                       title_func=test_message,
                                       options=OrderedDict([
                                           ("Да", State.NO_PROBLEM),
                                           ("Нет", State.PROBLEM),
                                       ]),
                                       photo='https://images.app.goo.gl/tiWDtYXqCCEKDWWH9',
                                       caption=messages['instruction']['text']
                                       ),

            # Проблемы с принтером
            State.PRINTER: MenuTransition(title=messages['Printer']['text'],
                                          options=OrderedDict([
                                              ("Принтер проблема 1", State.PRINTER_1),
                                              ("Принтер проблема 2",  State.PRINTER_2),
                                          ])),

            State.PRINTER_1: MenuTransition(title='Проблема с Принтером 1\nВариант решения\nПомогло ли?',
                                            title_func=test_message,
                                            options=OrderedDict([
                                                ("Да", State.NO_PROBLEM),
                                                ("Нет", State.PROBLEM),
                                            ]),
                                            photo='https://images.app.goo.gl/tiWDtYXqCCEKDWWH9',
                                            caption=messages['instruction']['text']
                                            ),

            State.PRINTER_2: MenuTransition(title='Проблема с Принтером 2\nВариант решения\nПомогло ли?',
                                            title_func=test_message,
                                            options=OrderedDict([
                                                ("Да", State.NO_PROBLEM),
                                                ("Нет", State.PROBLEM),
                                            ]),
                                            photo='https://images.app.goo.gl/tiWDtYXqCCEKDWWH9',
                                            caption=messages['instruction']['text']
                                            ),

            # Проблемы с интернетом
            State.INTERNET: MenuTransition(title=messages['Internet']['text'],
                                           options=OrderedDict([
                                               ("Интернет проблема 1", State.INTERNET_1),
                                               ("Интернет проблема 2",  State.INTERNET_2),
                                           ])),

            State.INTERNET_1: MenuTransition(title='Проблема с Интернетом 1\nВариант решения\nПомогло ли?',
                                             title_func=test_message,
                                             options=OrderedDict([
                                                ("Да", State.NO_PROBLEM),
                                                ("Нет", State.PROBLEM),
                                             ]),
                                             photo='https://images.app.goo.gl/tiWDtYXqCCEKDWWH9',
                                             caption=messages['instruction']['text']
                                             ),

            State.INTERNET_2: MenuTransition(title='Проблема с Интернетом 2\nВариант решения\nПомогло ли?',
                                             title_func=test_message,
                                             options=OrderedDict([
                                                ("Да", State.NO_PROBLEM),
                                                ("Нет", State.PROBLEM),
                                             ]),
                                             photo='https://images.app.goo.gl/tiWDtYXqCCEKDWWH9',
                                             caption=messages['instruction']['text']
                                             ),

            # Проблемы с телефоном
            State.PHONE: MenuTransition(title=messages['Phone']['text'],
                                        options=OrderedDict([
                                            ("Телефон проблема 1", State.PHONE_1),
                                            ("Телефон проблема 2", State.PHONE_2),
                                        ])),

            State.PHONE_1: MenuTransition(title='Проблема с Телефоном 1\nВариант решения\nПомогло ли?',
                                          title_func=test_message,
                                          options=OrderedDict([
                                              ("Да", State.NO_PROBLEM),
                                              ("Нет", State.PROBLEM),
                                          ]),
                                          photo='https://images.app.goo.gl/tiWDtYXqCCEKDWWH9',
                                          caption=messages['instruction']['text']
                                          ),

            State.PHONE_2: MenuTransition(title='Проблема с Телефоном 2\nВариант решения\nПомогло ли?',
                                          title_func=test_message,
                                          options=OrderedDict([
                                              ("Да", State.NO_PROBLEM),
                                              ("Нет", State.PROBLEM),
                                          ]),
                                          photo='https://images.app.goo.gl/tiWDtYXqCCEKDWWH9',
                                          caption=messages['instruction']['text']
                                          ),

            State.NO_PROBLEM: MenuTransition(
                                             title_func=no_problem,
                                             options=OrderedDict([]),
                                             ),

            State.PROBLEM: MenuTransition(

                                          title_func=problem,
                                          options=OrderedDict([])
                                          ),

        }
        super().__init__(token, State.MENU, transitions)


def test_message(data):
    print(f'test message data: {data}')
    text = 'Алгоритм действий:\n' \
           '- Пункт 1\n' \
           '- Пункт 2\n' \
           '- Пункт 3\n' \
           'Помог ли данный совет в решении проблемы?'
    return text


def no_problem(data):
    print(f'no problem data: {data}')
    text = 'Поздравляем, ваша проблема решена!\nНажмите /start если у вас остались еще проблемы.'
    return text


def problem(data):
    print(f'problem data: {data}')
    text = 'Для решения данной проблемы обратитесь к сотруднику техподдержки\n' \
           'Контакты сотрудника:\n' \
           'ФИО\n' \
           'телефон'
    return text


if __name__ == "__main__":
    main()
