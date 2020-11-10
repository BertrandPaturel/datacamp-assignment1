# noqa: D100
import numpy as np


def max_index(X):
    """Return the index of the maximum in a numpy array.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        The input array.

    Returns
    -------
    i : int
        The row index of the maximum.

    j : int
        The column index of the maximum.

    Raises
    ------
    ValueError
        If the input is not a numpy error or
        if the shape is not 2D.
    """
    i = 0
    j = 0

    # TODO
    if not isinstance(X, np.ndarray):
        raise ValueError('X is not an array')

    if len(X.shape) != 2:
        raise ValueError('X is not a 2D vector')

    i = X.argmax(axis=0)
    j = X.argmax(axis=1)

    return i, j


def wallis_product(n_terms):
    """Implement the Wallis product to compute an approximation of pi.

    See:
    https://en.wikipedia.org/wiki/Wallis_product

    Parameters
    ----------
    n_terms : int
        The number of products to approximate pi.

    Returns
    -------
    res : int
        The wallis product of rank n_terms.
    """
    # XXX : The n_terms is an int that corresponds to the number of
    # terms in the product. For example 10000.

    i = 1
    pi = 2

    while i <= n_terms:
        pi = pi * (2 * (i) ^ 2) / ((2 * (i) ^ 2) - 1)
        i += 1

    return pi
