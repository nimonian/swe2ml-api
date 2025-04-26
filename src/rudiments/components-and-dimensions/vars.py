import sympy as sp
import random
import src.utils as utils


def generate_vars():
    n = random.choice([2, 3, 4, 5])
    v = [random.randint(-10, 10) for _ in range(n)]
    k = random.randrange(0, n)
    kth = ["first", "second", "third", "fourth", "fifth"][k]
    answer = v[k] * n
    return locals()
