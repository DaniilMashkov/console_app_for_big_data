import time
import pandas as pd
import os
import shutil


def sell(*args: tuple) -> None:
    """При нахождении нужной строки меняет дату на текущую,
    Добавляет цену продажи к общей сумме. Перезаписывает файл в любом случае"""

    current_date = time.strftime('%Y-%m%d', time.localtime())
    chunk = pd.read_csv(f'data/{args[3]}.csv', chunksize=100_000)

    for df in chunk:

        df.loc[(df['cai'] == args[0]) & (df['region'] == args[1]), 'amount'] += args[2]
        df.loc[(df['cai'] == args[0]) & (df['region'] == args[1]), 'last_sale'] = current_date

        if os.path.exists(f'cache/{args[3]}.csv'):
            df.to_csv(f'cache/{args[3]}.csv', index=False, mode='a', header=False)
        else:
            df.to_csv(f'cache/{args[3]}.csv', index=False, mode='w')

    os.replace(f'cache/{args[3]}.csv', f'data/{args[3]}.csv')

    try:
        """Очищает кэш, если в нём есть неактуальная информация"""
        shutil.rmtree('cache/')
    except:
        pass
