import math
import sys


def list_mean(L):

    if L is None:
        raise ValueError("List cannot be \'None\'.")

    if len(L) == 0:
        raise ValueError("List cannot be empty.")

    try:
        mean = sum(L) / len(L)
    except TypeError:
        raise TypeError("List must only contain numeric values.")

    return mean


def list_stdev(L):

    mean = list_mean(L)
    var = sum(pow(el - mean, 2) for el in L) / len(L)
    std = math.sqrt(var)

    return std
