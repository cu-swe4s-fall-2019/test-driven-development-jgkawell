import math


def list_mean(L):

    if L is None:
        return None

    if len(L) == 0:
        return None

    try:
        mean = sum(L) / len(L)
    except TypeError:
        raise TypeError("List must only contain numeric values.")

    return mean


def list_stdev(L):

    mean = list_mean(L)

    if mean is None:
        return None

    var = sum(pow(el - mean, 2) for el in L) / len(L)
    std = math.sqrt(var)

    return std
