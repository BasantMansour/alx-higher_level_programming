#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for p in matrix:
        if len(p) == 0:
            print()
        for n in range(len(p)):
            print('{:d}'.format(p[n]),
                  end='\n' if n == len(p) - 1 else ' ')
