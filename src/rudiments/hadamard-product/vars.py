import sympy as sp
import random
import src.utils as utils


def generate_vars():
    n = random.choice([2, 3])
    u = [random.randint(-10, 10) for _ in range(n)]
    v = [random.randint(-10, 10) for _ in range(n)]
    w = [x * y for x, y in zip(u, v)]
    b, a = max(w), min(w)
    answer = b - a

    return locals()
