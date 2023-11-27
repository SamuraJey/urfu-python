import numpy as np
import pandas as pd
from numpy.testing import assert_equal, assert_array_equal
from pandas.testing import assert_frame_equal


def nearest_value(X, a):
    distances = np.abs(X - a)
    min_distance = np.min(distances)
    closest_elements = X[distances == min_distance]
    ew = np.min(closest_elements)
    return np.min(closest_elements)


######################################################
assert_equal(
    nearest_value(np.array([-1,  0]), -0.5),
    -1)
######################################################
assert_equal(
    nearest_value(np.array([[[1], [2], [3]], [[4], [5], [6]]]), 4.5),
    4)
######################################################
assert_equal(
    nearest_value(np.array([[1,  2, 13],
                            [15,  6,  8],
                            [7, 18,  9]]), 7.2),
    7)
######################################################
assert_equal(
    nearest_value(np.array([[-1,  -2],
                            [-15,  -6]]), -100),
    -15)
######################################################
assert_equal(
    nearest_value(np.array([[2,  2],
                            [12,  12]]), 7),
    2)
######################################################
assert_equal(
    nearest_value(np.array([[-2,  -2],
                            [-12,  -12]]), -7),
    -12)
######################################################
