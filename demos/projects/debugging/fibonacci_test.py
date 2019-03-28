#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: mxh @time:2019/3/28 10:14
"""
from demos.projects.debugging import math_tricks


def get_odd_fibs(num):
    r"""
    >>> get_odd_fibs(100*100)
    [1, 1, 3, 5, 13, 21, 55, 89, 233, 377, 987, 1597, 4181, 6765]
    """
    data = []
    fibs = math_tricks.fibonacci()
    odd_fibs = math_tricks.odd_numbers(fibs)
    for o in odd_fibs:
        if o > num:
            break

        data.append(o)
    return data


def get_fibs_in(num):
    r"""
    >>> get_fibs_in(100)
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    data, fibs = [], math_tricks.fibonacci()
    for i, f in enumerate(fibs):
        if f > num:
            break
        # print("index==", i)
        data.append(f)
    return data

if __name__ == '__main__':
    print(get_odd_fibs(100 * 100))
    print(get_fibs_in(100))