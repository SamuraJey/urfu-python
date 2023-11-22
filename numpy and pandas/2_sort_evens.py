import numpy as np


def sort_evens(A):
    div_by_five = A[A % 2 == 0]
    not_div = A[A % 2 != 0]
    sorted_div = np.sort(div_by_five)

    return np.concatenate((sorted_div, not_div))



######################################################
assert_array_equal(sort_evens(np.array([])), np.array([]))
######################################################
assert_array_equal(sort_evens(np.array([2, 0])), np.array([0, 2]))
######################################################
assert_array_equal(sort_evens(
    np.array([9, 3, 1, 5, 7])), np.array([9, 3, 1, 5, 7]))
######################################################
assert_array_equal(sort_evens(
    np.array([8, 12, 4, 10, 6, 2])), np.array([2, 4, 6, 8, 10, 12]))
######################################################