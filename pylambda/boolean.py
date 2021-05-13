# coding: utf-8
IDENTITY = lambda x: x

# boolean values
TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y

# basic boolean operations
NOT = lambda x: x(FALSE)(TRUE)
AND = lambda x: lambda y: x(y)(FALSE)
OR = lambda x: lambda y: x(TRUE)(y)
XOR = lambda x: lambda y: x(y(FALSE)(TRUE))(y(TRUE)(FALSE))

# condition
IF = lambda c: lambda x: lambda y: c(x)(y)
