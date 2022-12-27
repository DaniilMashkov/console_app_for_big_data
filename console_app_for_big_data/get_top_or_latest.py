import pandas as pd
import os


def get_top_or_latest(*args) -> None:
    """Сортирует по 100к строк, записывает промежуточный результат в файл,
    полученный результат снова сортируется и записывается в кэш"""

    chunk = pd.read_csv(args[2],
                        chunksize=100_000, usecols=['cai', 'region', 'last_sale', 'amount'])
    keyword = 'amount' if args[0] == 'top' else 'last_sale'

    for df in chunk:
        df.sort_values(by=keyword, ascending=False)[:args[1]]. \
            to_csv('cache/sorted.csv', index=False, mode='a')

    sorted_chunk = pd.read_csv('cache/sorted.csv', chunksize=100_000,
                               na_values=['cai', 'region', 'last_sale', 'amount'])

    for df in sorted_chunk:
        df.sort_values(by=keyword, ascending=False)[:args[1]]. \
            to_csv(f'cache/{args[:2]}.csv', index=False, mode='w')

    os.remove('cache/sorted.csv')
