# coding: utf-8
from .booleans import TRUE, FALSE

# pair
PAIR = lambda x: lambda y: lambda z: z(x)(y)
FIRST = lambda p: p(TRUE)
SECOND = lambda p: p(FALSE)
