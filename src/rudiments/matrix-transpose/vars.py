import sympy as sp
import random
import src.utils as utils


def generate_vars():
    r = random.randint(2, 4)
    c = random.randint(2, 4)
    A = random.choice("ABCDMNRS")
    M = sp.Matrix([[random.randint(-10, 10) for _ in range(c)] for _ in range(r)])
    N = M.transpose()
    r1, r2 = random.randrange(c), random.randrange(c)
    c1, c2 = random.randrange(r), random.randrange(r)
    answer = N[r1, c1] * N[r2, c2]
    return locals()
