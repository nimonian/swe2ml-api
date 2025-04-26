import sympy as sp
import random
import src.utils as u


def generate_vars():
    a, c = (random.randint(2, 10) for _ in range(2))
    b = u.randex(2, 10, [a])
    answer = 0

    return locals()
