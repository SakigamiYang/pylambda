# coding: utf-8
def incr(x: int) -> int:
    return x + 1


def decode_number(f) -> int:
    incr = lambda x: x + 1
    return f(incr)(0)
