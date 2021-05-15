# coding: utf-8
from .combinators import Y
from .natural import PRED, ADD, MUL, ZERO, ONE, TWO, ISZERO, LTE

# recursive
FACT = Y(
    lambda f: lambda n: ISZERO(n)
    (lambda _: ONE)
    (lambda _: MUL(n)(f(PRED(n))))
    (ZERO)
)

FIB = Y(
    lambda f: lambda n: LTE(n)(TWO)
    (lambda _: ONE)
    (lambda _: ADD(f(PRED(n)))(f(PRED(PRED(n)))))
    (ZERO)
)
