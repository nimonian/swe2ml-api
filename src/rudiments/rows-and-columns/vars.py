import sympy as sp
import random
import src.utils as utils


def generate_vars():
    r = random.randint(2, 5)
    c = random.randint(2, 5)
    A = random.choice("ABCDMNRST")
    M = sp.Matrix([[random.randint(-10, 10) for _ in range(c)] for _ in range(r)])
    r1, r2 = random.randrange(r), random.randrange(r)
    c1, c2 = random.randrange(c), random.randrange(c)
    answer = M[r1, c1] * M[r2, c2]
    return locals()
