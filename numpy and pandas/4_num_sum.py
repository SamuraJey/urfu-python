import numpy as np
import pandas as pd
from numpy.testing import assert_equal, assert_array_equal
from pandas.testing import assert_frame_equal


def num_sum(np_arr: np.ndarray) -> np.ndarray:
    num_digits = len(str(np.max(np_arr)))
    print(f"num_digits: {num_digits}")
    powers_of_10 = 10 ** np.arange(num_digits)[:, np.newaxis]
    print(f"powers_of_10:\n {powers_of_10}")
    digits = (np_arr // powers_of_10) % 10
    print(f"digits:\n {digits}")
    sum_of_digits = np.sum(digits, axis=0)
    print(f"sum_of_digits: {sum_of_digits}")

    return sum_of_digits


######################################################
assert_array_equal(num_sum(np.array([82])), np.array([10]))
######################################################
assert_array_equal(num_sum(np.array([1241, 354, 121])), np.array([8, 12, 4]))
######################################################
assert_array_equal(
    num_sum(np.array([1, 22, 333, 4444, 55555])), np.array([1, 4, 9, 16, 25]))
######################################################
