import numpy as np
import pandas as pd
from numpy.testing import assert_equal, assert_array_equal
from pandas.testing import assert_frame_equal


def replace_nans(X):
    medians = np.nanmedian(X, axis=0)
    nan_mask = np.isnan(X)
    medians[np.isnan(medians)] = 0
    X = np.where(nan_mask, medians, X)

    return X


######################################################
assert_array_equal(replace_nans(
    np.array([[np.nan], [np.nan],  [np.nan]])),
    np.array([[0.], [0.], [0.]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[0, 42,  42]])),
    np.array([[0, 42, 42]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[np.nan], [1], [np.nan]])),
    np.array([[1.], [1.], [1.]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[4], [1],  [np.nan]])),
    np.array([[4], [1], [2.5]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[np.nan, np.nan,  np.nan],
              [4, np.nan,       5],
              [np.nan,      8,  np.nan]]).T),
    np.array([[0., 0., 0.],
              [4., 4.5, 5.],
              [8., 8., 8.]]).T
)
######################################################
