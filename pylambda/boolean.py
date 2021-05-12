# coding: utf-8
IDENTITY = lambda x: x
IF = IDENTITY

# boolean values
TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y

# basic boolean operations
NOT = lambda x: x(FALSE)(TRUE)
AND = lambda x: lambda y: x(y)(FALSE)
OR = lambda x: lambda y: x(TRUE)(y)

# additional boolean operations
XOR = lambda x: lambda y: x(y(FALSE)(TRUE))(y(TRUE)(FALSE))
XNOR = lambda x: lambda y: NOT(XOR(x)(y))
