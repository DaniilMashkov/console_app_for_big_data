import pandas as pd
import os


def get_region_top(*args) -> None:
    """Читает файл по 100к строк, группирует строки по региону, суммируя все его продажи и
      сохраняя промежуточный результат в файл. Операция повторяется и сохраняется в кэш"""

    chunk = pd.read_csv(args[2], chunksize=100_000, usecols=['region', 'amount'])

    for df in chunk:
        df.groupby('region')['amount'].sum().reset_index('region'). \
            to_csv('cache/sorted.csv', mode='a', index=False)

    result = pd.read_csv('cache/sorted.csv', na_values=['region', 'amount'])

    result.groupby('region')['amount'].sum().reset_index('region'). \
        sort_values(by='amount', ascending=False)[:args[1]]. \
        to_csv(f"cache/{args[:2]}.csv", mode='w', index=False)

    os.remove('cache/sorted.csv')

