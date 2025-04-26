import sympy as sp
import random
import src.utils as utils
from functools import reduce


def generate_vars():
    m = random.randint(2, 3)
    n = random.randint(2, 3)
    A = [[random.randint(-10, 10) for _ in range(m)] for _ in range(n)]
    B = [[random.randint(-10, 10) for _ in range(m)] for _ in range(n)]
    C = [[x + y for x, y in zip(a, b)] for a, b in zip(A, B)]

    prod = lambda L: reduce(lambda x, y: x * y, L)
    answer = prod(map(prod, C))

    return locals()
