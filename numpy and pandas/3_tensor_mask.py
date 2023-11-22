import numpy as np
import pandas as pd
from numpy.testing import assert_equal, assert_array_equal
from pandas.testing import assert_frame_equal

def tensor_mask(X: np.ndarray, mask: np.ndarray) -> np.ndarray:
    return X ^ mask


######################################################
X = np.zeros(9, dtype=int).reshape((1,3,3))
mask = np.zeros(9, dtype=int).reshape((3,3))
assert_array_equal(tensor_mask(X, mask), np.zeros(9, dtype=int).reshape((1,3,3)))
######################################################
X = np.zeros(9*3, dtype=int).reshape((3,3,3))
mask = np.ones(9, dtype=int).reshape((3,3))
assert_array_equal(tensor_mask(X, mask), np.ones(9*3, dtype=int).reshape((3,3,3)))
######################################################
X = np.array([[[ 1, 0, 1],
               [ 1, 1, 1],
               [ 0, 0, 1]]])
mask = np.array([[1, 1, 0],
                 [1, 1, 0],
                 [1, 1, 0]])
assert_array_equal(tensor_mask(X, mask), 
                   np.array([[[0, 1, 1],
                             [0, 0, 1],
                             [1, 1, 1]]]))
######################################################