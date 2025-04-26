import sympy as sp
import random
import src.utils as utils


def generate_vars():
    n = random.choice([2, 3, 4])
    l = utils.randex(-10, 11, [0])
    u = [random.randint(-10, 10) for _ in range(n)]
    v = [l * x for x in u]
    k = random.randrange(0, n)
    kth = ["first", "second", "third", "fourth"][k]
    answer = v[k]

    return locals()
