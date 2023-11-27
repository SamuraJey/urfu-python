import datetime
import numpy as np
import pandas as pd
from numpy.testing import assert_equal, assert_array_equal
from pandas.testing import assert_frame_equal
import dateutil.relativedelta

months = {
    "января": 1,
    "февраля": 2,
    "марта": 3,
    "апреля": 4,
    "мая": 5,
    "июня": 6,
    "июля": 7,
    "августа": 8,
    "сентября": 9,
    "октября": 10,
    "ноября": 11,
    "декабря": 12,
}


def get_date(str_date: str) -> datetime.date:
    split_date = str_date[:-3].split()
    year = int(split_date[2])
    month = months[split_date[1]]
    day = int(split_date[0])
    return datetime.date(year, month, day)


def get_delta(df: pd.DataFrame) -> pd.DataFrame:
    return dateutil.relativedelta.relativedelta(get_date(df["Дата смерти"]), get_date(df["Дата рождения"])).years


def rus_feature(df: pd.DataFrame) -> pd.DataFrame:
    df["Полных лет"] = df.apply(get_delta, axis=1)
    return df


######################################################
names = pd.DataFrame({'Имя': ['Никола Тесла', 'Альберт Эйнштейн'],
                      'Дата рождения': ['10 июля 1856 г.', '14 марта 1879 г.'],
                      'Дата смерти':  ['7 января 1943 г.', '18 апреля 1955 г.']})
answer = pd.DataFrame({'Имя': ['Никола Тесла', 'Альберт Эйнштейн'],
                       'Дата рождения': ['10 июля 1856 г.', '14 марта 1879 г.'],
                       'Дата смерти':  ['7 января 1943 г.', '18 апреля 1955 г.'],
                       'Полных лет': [86, 76]})
assert_frame_equal(
    rus_feature(names),
    answer
)
######################################################
names = pd.DataFrame({'Имя': ['Никола Тесла'],
                      'Дата рождения': ['10 июля 1856 г.'],
                      'Дата смерти':  ['7 января 1857 г.']})
answer = pd.DataFrame({'Имя': ['Никола Тесла'],
                       'Дата рождения': ['10 июля 1856 г.'],
                       'Дата смерти':  ['7 января 1857 г.'],
                       'Полных лет': [0]})
assert_frame_equal(
    rus_feature(names),
    answer
)
######################################################
names = pd.DataFrame({'Имя': ['Никола Тесла'],
                      'Дата рождения': ['1 января 2000 г.'],
                      'Дата смерти':  ['31 декабря 2000 г.']})
answer = pd.DataFrame({'Имя': ['Никола Тесла'],
                       'Дата рождения': ['1 января 2000 г.'],
                       'Дата смерти':  ['31 декабря 2000 г.'],
                       'Полных лет': [0]})
assert_frame_equal(
    rus_feature(names),
    answer
)
