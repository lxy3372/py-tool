#!/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'Riky'


def insert_sort(lists):
    for i in range(0, len(lists)):
        tmp = lists[i]
        key = i - 1
        while key >= 0 and tmp < lists[key]:
            lists[key + 1] = lists[key]
            key -= 1
        lists[key + 1] = tmp
    return lists


if __name__ == '__main__':
    lists = [4, 1, 2, 9, 3, 10, 6, 5, 8, 0, 7]
    print insert_sort(lists)

