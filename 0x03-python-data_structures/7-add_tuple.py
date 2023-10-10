#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a + ('0', '0')
    b1 = tuple_b + ('0', '0')

    su1 = int(a1[0]) + int(b1[0])
    su2 = int(a1[1]) + int(b1[1])

    return su1, su2
