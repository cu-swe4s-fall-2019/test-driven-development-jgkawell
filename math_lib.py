
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
    return None
