import sympy as sp
from random import randrange
import src.utils as u


def generate_vars():
    x, p, q = sp.symbols("x p q")

    P1, Q1 = u.randex(-3, 4, [0, 1]), u.randex(-10, 11, [0])
    F1 = P1 * x + Q1

    P2, Q2 = u.randex(-3, 4, [0]), u.randex(-10, 11, [0, Q1])
    F2 = P2 * x + Q2

    F = F1 * F2

    d1 = sp.gcd(P1, Q1) * u.sgn(P1)
    d2 = sp.gcd(P2, Q2) * u.sgn(P2)
    d = d1 * d2

    p1, q1 = P1 / d1, Q1 / d1
    p2, q2 = P2 / d2, Q2 / d2

    f1 = p1 * x + q1
    f2 = p2 * x + q2
    f = f1 * f2

    a = p1 * p2
    b = p1 * q2 + q1 * p2
    c = q1 * q2

    r1 = sp.Rational(-q1, p1)
    r2 = sp.Rational(-q2, p2)

    r1, r2 = sorted([r1, r2])

    k1 = u.randex(1, 6, [0]) * a
    k2 = u.randex(1, 6, [k1, 0]) * a

    answer = k1 * r1 + k2 * r2

    return locals()
