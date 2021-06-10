# coding: utf-8
from .booleans import IDENTITY, TRUE, FALSE, NOT, AND
from .combinators import Y

# arithmetic
SUCC = lambda n: lambda f: lambda x: f(n(f)(x))
# Because there are no negative numbers in the concept - "natural numbers",
# any predecessor of ZERO are always ZERO.
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

# more arithmetic
DIV = Y(
    lambda f: lambda m: lambda n: LT(m)(n)
    (lambda _: ZERO)
    (lambda _: SUCC(f(SUB(m)(n))(n)))
    (ZERO)
)

MOD = Y(
    lambda f: lambda m: lambda n: LT(m)(n)
    (lambda _: m)
    (lambda _: f(SUB(m)(n))(n))
    (ZERO)
)

EVEN = lambda n: ISZERO(MOD(n)(TWO))
ODD = lambda n: NOT(EVEN(n))
