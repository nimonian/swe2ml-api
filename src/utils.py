from decimal import Decimal
import random
import sympy as sp
from functools import reduce


def randex(a: int, b: int, L: list) -> int:
    """
    Generate a random integer within a specified range that is not in a given exclusion list.

    Parameters
    ==========
    a : int
        The inclusive start of the range.
    b : int
        The exclusive end of the range.
    L : list
        A list of integers to be excluded from the random selection.

    Returns
    =======
    int
        A randomly chosen integer from the range [a, b) that is not in the list L.

    Raises
    ======
    IndexError
        If all numbers in the range are in the exclusion list, making the list of choices empty.

    """

    R = list(x for x in range(a, b) if x not in L)
    return random.choice(R)


def add_num(n):
    """
    Return a string for x as a signed number, with negative values
    preceded by a minus sign and positive values preceded by a plus sign.

    Examples
    ========
    >>> add(-1)
    '- 1'
    >>> add(1)
    '+ 1'
    """
    symbol = "-" if n < 0 else "+"
    value = -n if n < 0 else n
    return f"{symbol} {value}"


def add_term(n, var=1):
    """
    Return a string for the term n * var as a signed number, with negative values
    preceded by a minus sign and positive values preceded by a plus sign.

    Parameters
    ==========
    n : int
        The coefficient of the term.
    var : sympy Expr
        The variable of the term.

    Returns
    =======
    str
        The string representation of the term.
    """
    symbol = "-" if n < 0 else "+"
    return f"{symbol} {sp.latex(abs(n) * var)}"


def factored_int(x):
    """
    Return a string representation of an integer. If the integer is -1, return a minus sign.
    Otherwise, return the sp.latex representation of the integer.

    Parameters
    ==========
    x : int
        The integer to be represented.

    Returns
    =======
    str
        '-' if x is -1, otherwise the sp.latex string representation of x.

    Examples
    ========
    >>> factored_int(-1)
    '-'
    >>> factored_int(3)
    '3'
    """

    return "-" if x == -1 else sp.latex(x)


def sgn(x):
    """
    Return the sign of a number.

    Parameters
    ==========
    x : int or float
        The number for which the sign is to be determined.

    Returns
    =======
    int
        -1 if x is negative, 1 if x is positive, 0 if x is zero.

    Examples
    ========
    >>> sgn(-5)
    -1
    >>> sgn(0)
    0
    >>> sgn(3)
    1
    """

    if x < 0:
        return -1

    if x > 0:
        return 1

    return 0


def sgn_symbol(n):
    if n >= 0:
        return "+"

    return "-"


def prod(L):
    return reduce(lambda x, y: x * y, L)


def brackets_if_negative(x):
    return f"({str(x)})" if x < 0 else str(x)


def as_coeff(n):
    if n == 1:
        return ""
    if n == -1:
        return "-"

    return sp.latex(n)


def as_operation(n):
    if n == 1:
        return "+"
    if n == -1:
        return "-"
    return sgn_symbol(n) + sp.latex(abs(n))


def sig_figs(x, n):
    return Decimal(f"{float(x):.{n}g}")


def abs(x):
    return x if x >= 0 else -x
