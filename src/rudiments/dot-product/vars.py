import sympy as sp
import random
import src.utils as utils


def generate_vars():
    u = random.randint(1, 100) / 10
    v = random.randint(1, 100) / 10
    t = random.randint(-100, 100) / 100
    answer = ((u * 10) * (v * 10) * (t * 100)) / (10 * 10 * 100)
    return locals()
