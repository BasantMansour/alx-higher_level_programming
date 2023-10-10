#!/usr/bin/env python3
def no_c(my_string):
    t = ""
    for j in range(len(my_string)):
        if (my_string[j] != 'c' and my_string[j] != 'C'):
            t += my_string[j]
            return t
