import sympy as sp
import random
import src.utils as utils


def generate_vars():
    n = random.choice([2, 3])
    a = utils.randex(-10, 11, [0])
    b = utils.randex(-10, 11, [0, a if a == 1 else 0])
    u = [random.randint(-10, 10) for _ in range(n)]
    v = [random.randint(-10, 10) for _ in range(n)]
    au = [a * x for x in u]
    bv = [b * y for y in v]
    w = [x + y for x, y in zip(au, bv)]
    answer = utils.prod(w)

    return locals()
