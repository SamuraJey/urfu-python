import numpy as np
import pandas as pd
from numpy.testing import assert_equal, assert_array_equal
from pandas.testing import assert_frame_equal


def ZOOtable(zoo: dict) -> pd.DataFrame:
    df = pd.DataFrame.from_dict(zoo, orient='index')

    df.insert(0, 'Type', df.index)
    # print(f'1:\n{df}\n')
    df.sort_values('Type', inplace=True)
    # print(f'2:\n{df}\n')
    df = df.reindex(sorted(df.columns), axis=1)
    # print(f'3:\n{df}\n')
    df.reset_index(drop=True, inplace=True)
    # print(f'4:\n{df}\n')
    df.dropna(axis=1, how='any', inplace=True)
    # print(f'5:\n{df}\n')

    return df


######################################################
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
df = ZOOtable(ZOO)

assert_frame_equal(
    df.reset_index(drop=True),
    answer
)
######################################################
ZOO = {
    'cat': {'color': 'black'},
    'dog': {'age': 6}
}
answer = pd.DataFrame(
    {
        'Type': ['cat', 'dog']
    }
)

df = ZOOtable(ZOO)

assert_frame_equal(
    df.reset_index(drop=True),
    answer
)
######################################################
