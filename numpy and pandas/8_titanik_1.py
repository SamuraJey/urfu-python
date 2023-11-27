import numpy as np
import pandas as pd
from numpy.testing import assert_equal, assert_array_equal
from pandas.testing import assert_frame_equal


def men_stat(df: pd.DataFrame) -> (float, float, float, float):
    ages_of_dead_males = df[(df['Survived'] == 0) &
                            (df['Sex'] == 'male')]['Age'].dropna()
    mean = ages_of_dead_males.mean()
    median = ages_of_dead_males.median()
    maximum = ages_of_dead_males.max()
    minimum = ages_of_dead_males.min()
    return mean, median, maximum, minimum


data = pd.read_csv('numpy and pandas/titanic_train.csv',
                   index_col='PassengerId')
print(men_stat(data))
