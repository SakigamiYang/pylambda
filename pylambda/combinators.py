# coding: utf-8
from .boolean import IDENTITY, TRUE

# combinators

# SKI combinator
# All operations in lambda calculus can be encoded via abstraction elimination into the SKI calculus
# as binary trees whose leaves are one of the three symbols S, K, and I (called combinators).
#
# But SKI system is not the minimum system, because I = SKK or SKS or (SK whatever).
# But also, SK system is not the minimum system, if we define the iota combinator as
#   ιx = xSK
# we will get:
#   I = SK(KK) = SSKK = ιSK = ιι,
#   K = SKSK = ι(SK) = ι(ISK) = ι(ιιSK) = ι(ι(ιι)),
#   S = KSK = ιK = ι(ι(ι(ιι)))

# Ix = x
I = IDENTITY
# When applied to any argument x,
# yields a one-argument constant function,
# (Kx)y = x
K = TRUE
# Substitution operator.
# It takes three arguments and then returns the first argument applied to the third,
# which is then applied to the result of the second argument applied to the third.
S = lambda x: lambda y: lambda z: x(z)(y(z))

# Fixed-point combinator
#   Y = λf.(λx.f(x x)) (λx.f(x x))
# Proof:
#   Y g = λf.(λx.f(x x)) (λx.f(x x)) g
#       = (λx.g(x x)) (λx.g(x x))  (by β-reduction of λf: applied Y to g)
#       = (λy.g(y y)) (λx.g(x x))  (by α-conversion of left function: rename x to y)
#       = g ((λx.g(x x)) (λx.g(x x)))  (by β-reduction of λx: applied left function to right function)
#       = g (Y g)
#
# We also have: Y = S(K(SII))(S(S(KS)K)(K(SII)))
#
# In fact, the implementation here is an operator called Z, where
#   Z = λf.(λx.f(λy.x x y)) (λf.(λy.x x y))
# because that Y needs "lazy evaluation".
# In Python, if we run Y immediately, it will BOOM by infinite loop.
Y = lambda f: (
    (lambda x: f(lambda y: x(x)(y)))
    (lambda x: f(lambda y: x(x)(y)))
)
