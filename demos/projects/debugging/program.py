from demos.projects.debugging import math_tricks
from collections.abc import Iterator


# print(isinstance(fibs, Iterator))


def get_odd_fibs(num):
    r"""
    >>> get_odd_fibs(1000)
    [1, 1, 3, 5, 13, 21, 55, 89, 233, 377, 987]
    """
    data = []
    fibs = math_tricks.fibonacci()
    odd_fibs = math_tricks.odd_numbers(fibs)
    for o in odd_fibs:
        if o > num:
            break

        data.append(o)
    return data


def get_fibs_in(within_num, index=None):
    """

    :param within_num: within_num （比如100）以内的fibonacci 数
    :param index: 前 index（11）个fibonacci数
    :return:
    """
    _index, data, fibs = [], [], math_tricks.fibonacci()
    if index:
        for i, f in enumerate(fibs, 1):
            if i > index:
                break
            _index.append(i)
            data.append(f)
    else:
        for i, f in enumerate(fibs, 1):
            if f > within_num:
                break
            _index.append(i)
            data.append(f)
    print(_index)
    return data


if __name__ == '__main__':
    # print(get_odd_fibs(1000))
    print(get_fibs_in(1000, index=11))
    # print(get_fibs_in(100))


