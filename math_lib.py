import math
import sys

"""
This library contains a couple statistics functions
for lists of numeric values.
"""


def list_mean(array):
    """
    Compute the mean of a given numeric list.
    Checks for None value or empty lists.

    Parameters
    ----------
    array : list of ints or doubles

    Returns
    ----------
    mean : The mean of the values in the given list

    """

    # Make sure the list is not None type
    if array is None:
        raise ValueError("List cannot be \'None\'.")
    # Make sure the list is not empty
    if len(array) == 0:
        raise ValueError("List cannot be empty.")
    # Try to find the mean but check for invalid types
    try:
        mean = sum(array) / len(array)
    except TypeError:
        raise TypeError("List must only contain numeric values.")

    return mean


def list_stdev(array):
    """
    Compute the standard deviation of a given numeric list.
    Checks for None value or empty lists.

    Parameters
    ----------
    array : list of ints or doubles

    Returns
    ----------
    stdev : The standard deviation of the values in the given list

    """

    # Find stdev using mean from method above
    mean = list_mean(array)
    var = sum(pow(el - mean, 2) for el in array) / len(array)
    stdev = math.sqrt(var)

    return stdev
