import sympy as sp
from random import randrange
import src.utils as u


def generate_vars():
    x, p, q = sp.symbols("x p q")
    p0 = u.randex(-10, 11, [0])
    q0 = randrange(-10, 11)
    p0, q0 = sorted([p0, q0])
    k1 = u.randex(1, 10, [0])
    k2 = u.randex(1, 10, [k1, 0])
    f = (x - p0) * (x - q0)
    f_exp = f.expand()
    answer = k1 * p0 + k2 * q0

    return locals()
