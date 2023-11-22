import numpy as np
import pandas as pd
from numpy.testing import assert_equal, assert_array_equal
from pandas.testing import assert_frame_equal


def ZOOtable(zoo):
    df = pd.DataFrame.from_dict(zoo, orient='index')

    # Добавляем колонку Type с типом животного
    df.insert(0, 'Type', df.index)
    # Сортируем строки по типу животного
    df.sort_values('Type', inplace=True)
    # Сортируем колонки в алфавитном порядке, кроме колонки Type
    df = df.reindex(sorted(df.columns), axis=1)
    # Сбрасываем индексы строк
    df.reset_index(drop=True, inplace=True)
    # Если в колонке есть NaN, то удаляем эту колонку
    df.dropna(axis=1, how='any', inplace=True)

    return df


ZOO = {
    'cat': {'color': 'black', 'tail_len': 50.0, 'injured': False},
    'dog': {'age': 6, 'tail_len': 30.5, 'injured': True}
}
answer = pd.DataFrame(
    {
        'Type': ['cat', 'dog'],
        'injured': [False, True],
        'tail_len': [50.0, 30.5]
    }
)


######################################################
ZOO = {
        'cat': {'color':'black', 'tail_len': 50.0, 'injured': False}, 
        'dog': {'age': 6, 'tail_len': 30.5, 'injured': True}
      }
answer = pd.DataFrame(
    {
     'Type':['cat', 'dog'], 
     'injured':[False, True], 
     'tail_len':[50.0, 30.5]
    }
)
df = ZOOtable(ZOO)

assert_frame_equal(
    df.reset_index(drop=True),
    answer
)
######################################################
ZOO = {
        'cat': {'color':'black'}, 
        'dog': {'age': 6}
      }
answer = pd.DataFrame(
    {
     'Type':['cat', 'dog']
    }
)

df = ZOOtable(ZOO)

assert_frame_equal(
    df.reset_index(drop=True),
    answer
)
######################################################