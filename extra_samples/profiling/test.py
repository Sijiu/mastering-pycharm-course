#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: mxh @time:2019/3/27 17:56
"""
import re


def get_line_words(fin):
    r"""
    :param name:
    :return: Hello name
    >>> get_line_words([': ."hello world, my name!\n', 'is matt.\n'])
    ['world', 'my', 'name', 'is', 'matt']
    """
    book_words = []
    word_re = re.compile(r'(\w*)')

    for line in fin:
        for word in line.split():
            # don't use match it checks start of line
            valid = word_re.search(word)
            if valid and valid.group(1):
                book_words.append(valid.group(1))

    # print(book_words)
    return book_words


def hello(name):
    r"""
    >>> hello("Bob")
    Hello Bob
    'Hello Bob'
    """
    hi = 'Hello ' + name
    print(hi)
    return hi

if __name__ == '__main__':
    # get_line_words([': ."hello world, my name!\n'])
    print(hello("Tom"))