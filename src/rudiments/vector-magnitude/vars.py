import sympy as sp
import random
import src.utils as utils


def generate_vars():
    n = random.choice([2, 3])
    v = [random.randint(-10, 10) for _ in range(n)]
    _v = random.choice("uvwpqrab")
    sq_sum = sum(x**2 for x in v)
    sq_sum_list = " + ".join(f"{utils.brackets_if_negative(x)}^2" for x in v)
    answer = str(sp.S(sq_sum**0.5).evalf(3))
    magnitude = random.choice(["length", "size", "magnitude", "absolute value"])

    return locals()
