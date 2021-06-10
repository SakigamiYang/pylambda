# coding: utf-8
from booleans import TRUE, FALSE, NOT, OR
from combinators import Y
from naturals import SUCC, PRED, GTE, ISZERO, ZERO
from pairs import PAIR, FIRST, SECOND

LIST = PAIR(TRUE)(TRUE)
EMPTY = lambda xs: FIRST(xs)
HEAD = lambda xs: FIRST(SECOND(xs))
TAIL = lambda xs: SECOND(SECOND(xs))
PREPEND = lambda xs: lambda x: PAIR(FALSE)(PAIR(x)(xs))
APPEND = Y(
    lambda f: lambda xs: lambda x: EMPTY(xs)
    (lambda _: PREPEND(xs)(x))
    (lambda _: PAIR(FALSE)(PAIR(HEAD(xs))(f(TAIL(xs))(x))))
    (TRUE)
)
REVERSE = Y(
    lambda f: lambda xs: EMPTY(xs)
    (lambda _: LIST)
    (lambda _: APPEND(f(TAIL(xs)))(HEAD(xs)))
    (TRUE)
)
MAP = Y(
    lambda f: lambda a: lambda xs: EMPTY(xs)
    (lambda _: LIST)
    (lambda _: PREPEND(f(a)(TAIL(xs)))(a(HEAD(xs))))
    (TRUE)
)
RANGE = Y(
    lambda f: lambda a: lambda b: GTE(a)(b)
    (lambda _: LIST)
    (lambda _: PREPEND(f(SUCC(a))(b))(a))
    (TRUE)
)
REDUCE = FOLD = Y(
    lambda f: lambda r: lambda l: lambda v: EMPTY(l)
    (lambda _: v)  # if list is empty, return accumulated value (v)
    # pass accumulated value (v) and head into reducer (r)
    # do reucing on tail of list (l) with a new accumulated value (v)
    (lambda _: f(r)(TAIL(l))(r(HEAD(l))(v)))
    (TRUE)
)
FILTER = lambda f: lambda l: (
    REDUCE
    (lambda x: lambda xs: f(x)(APPEND(xs)(x))(xs))
    (l)
    (LIST)
)
DROP = lambda n: lambda l: n(TAIL)(l)
TAKE = Y(lambda f: lambda n: lambda l: (
    OR(EMPTY(l))(ISZERO(n))
    (lambda _: LIST)
    (lambda _: (
        PREPEND(f(PRED(n))(TAIL(l)))
        (HEAD(l))
    ))
    (TRUE)
))
LENGTH = lambda l: REDUCE(lambda x: lambda n: SUCC(n))(l)(ZERO)
INDEX = Y(lambda f: lambda n: lambda l: (
    ISZERO(n)
    (lambda _: HEAD(l))
    (lambda _: f(PRED(n))(TAIL(l)))
    (TRUE)
))
ANY = Y(lambda f: lambda l: (
    EMPTY(l)
    (lambda _: FALSE)
    (lambda _: HEAD(l)(TRUE)(f(TAIL(l))))
    (TRUE)
))
ALL = Y(lambda f: lambda l: (
    EMPTY(l)
    (lambda _: TRUE)
    (lambda _: NOT(HEAD(l))(FALSE)(f(TAIL(l))))
    (TRUE)
))
