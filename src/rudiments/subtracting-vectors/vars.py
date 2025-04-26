import sympy as sp
import random
import src.utils as utils


def generate_vars():
    n = random.choice([2, 3])
    u = [random.randint(-10, 10) for _ in range(n)]
    v = [random.randint(-10, 10) for _ in range(n)]
    w = [y - x for y, x in zip(v, u)]

    sq_sum = sum(x**2 for x in w)
    sq_sum_list = " + ".join(f"{utils.brackets_if_negative(x)}^2" for x in w)
    answer = str(sp.S(sq_sum**0.5).evalf(3))

    return locals()
