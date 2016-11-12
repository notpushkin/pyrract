from collections import Iterable


def flatten(l):
    """
    Deep flattens a list, i. e. [[[1, 2, 3], [4, 5]], 6] -> [1, 2, 3, 4, 5, 6].

    Yields:
        items of the final sequence.
    """

    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


def iif(f):
    """
    Immediately-invoked function. Replaces the decorated function with
    its return value.
    """

    return f()
