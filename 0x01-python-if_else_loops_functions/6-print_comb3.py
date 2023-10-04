#!/usr/bin/python3
for d in range(0, 10):
    for t in range(d + 1, 10):
        if d == t:
            pass
        elif d == 8 and t == 9:
            print("{}{}".format(d, t))
        else:
            print("{}{}".format(d, t), end=", ")
