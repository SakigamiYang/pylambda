# coding: utf-8
from .boolean import IDENTITY, TRUE, FALSE, AND

# arithmetic
SUCC = lambda n: lambda f: lambda x: f(n(f)(x))
PRED = lambda n: n(lambda p: lambda z: z(SUCC(p(TRUE)))(p(TRUE)))(lambda z: z(ZERO)(ZERO))(FALSE)
ADD = lambda m: lambda n: n(SUCC)(m)
SUB = lambda m: lambda n: n(PRED)(m)
MUL = lambda m: lambda n: n(ADD(m))(ZERO)
EXP = lambda m: lambda n: n(m)

# Church numbers
# In Church's opinion, an isomorphism exists between natural numbers and counter for function application.
ZERO = FALSE
ONE = IDENTITY
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR = SUCC(THREE)
FIVE = ADD(TWO)(THREE)
SIX = MUL(TWO)(THREE)
SEVEN = SUCC(SUCC(SUCC(SUCC(SUCC(SUCC(ONE))))))
EIGHT = PRED(MUL(THREE)(THREE))
NINE = EXP(THREE)(TWO)
TEN = SUB(ADD(EIGHT)(THREE))(ONE)

# validates
ISZERO = lambda n: n(lambda _: FALSE)(TRUE)
GTE = lambda m: lambda n: ISZERO(SUB(n)(m))
LTE = lambda m: lambda n: ISZERO(SUB(m)(n))
GT = lambda m: lambda n: ISZERO(SUB(SUCC(n))(m))
LT = lambda m: lambda n: ISZERO(SUB(SUCC(m))(n))
EQ = lambda m: lambda n: AND(GTE(m)(n))(LTE(m)(n))

# advanced arithmetic
MIN = lambda m: lambda n: LTE(m)(n)(m)(n)
MAX = lambda m: lambda n: GTE(m)(n)(m)(n)
