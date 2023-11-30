import numpy as np
import pandas as pd
from numpy.testing import assert_equal, assert_array_equal
from pandas.testing import assert_frame_equal


def age_stat(df: pd.DataFrame) -> pd.DataFrame:
    answ = df.groupby(['Sex', 'Pclass'])
    answ = answ.median()["Age"]
    return answ


data = pd.read_csv('numpy and pandas/titanic_train.csv',
                   index_col='PassengerId')

print(age_stat(data))
