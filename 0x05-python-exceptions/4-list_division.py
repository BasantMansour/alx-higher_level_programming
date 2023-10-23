#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    y = 0
    n_list = []
    for y in range(list_length):
        try:
            r = my_list_1[y] / my_list_2[y]
        except TypeError:
            print("wrong type")
            r = 0
        except ZeroDivisionError:
            print("division by 0")
            r = 0
        except IndexError:
            print("out of range")
            r = 0
        finally:
            n_list.append(r)
    return n_list
