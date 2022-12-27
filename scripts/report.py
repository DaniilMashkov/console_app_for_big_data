import os
import os.path

import pandas as pd

from console_app_for_big_data.get_regions import get_region_top
from console_app_for_big_data.get_top_or_latest import get_top_or_latest


def get_report():
    data_path = 'data/michelin_data.csv'
    req = input("Выберете тип отчёта:\n1: top\n2: latest\n3: region\n")
    count = input('Сколько выводить значений?\n')

    if req == '1': req = 'top'
    if req == '2': req = 'latest'
    if req == '3': req = 'region'

    try:
        '''Выводится результат, если запрос есть в кэше'''

        read_csv(req, int(count), data_path[:2])

    except FileNotFoundError:
        if not os.path.exists('cache'):
            os.mkdir('cache')

        if req == 'top':
            get_top_or_latest('top', int(count), data_path)
            return read_csv('top', int(count), data_path[:2])

        if req == 'latest':
            get_top_or_latest('latest', int(count), data_path)
            return read_csv('latest', int(count), data_path[:2])

        if req == 'region':
            get_region_top('region', int(count), data_path)
            return read_csv('region', int(count), data_path[:2])

        else:
            return print('Такого отчёта нет')

    except ValueError:
        return print('Некорректный ввод\n')


def read_csv(*args):
    df = pd.read_csv(f'cache/{args[:2]}.csv')
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)
