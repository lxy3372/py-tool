#!/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'Riky'


def middle(sort_tuple, key, low=0, high=0):
    if high == 0:
        high = len(sort_tuple) - 1
    mid = int((high - low) / 2)
    while low < high:
        if sort_tuple[mid] > key:
            low = mid + 1
        elif sort_tuple[mid] > key:
            high = mid - 1
        else:
            return mid
        return middle(sort_tuple, key, low, high)
    else:
        return False


if __name__ == '__main__':
    sort_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 21, 44)
    print middle(sort_tuple, 9)

