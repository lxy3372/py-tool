#!/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'Riky'


def buddle(list):
    length = len(list)
    while (length > 0):
        for i in range(length - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        length -= 1
    return list


if __name__ == '__main__':
    list = [4, 6, 3, 2, 9, 1, 0, 7]
    print buddle(list)
