#!/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'Riky'


def select(lists):
    lenth = len(lists)
    for i in range(0, lenth):
        min = i
        for j in range(i + 1, lenth):
            if lists[j] < lists[min]:
                lists[j], lists[min] = lists[min], lists[j]
    return lists


if __name__ == "__main__":
    lists = [7, 2, 1, 5, 8, 4, 3]
    print select(lists=lists)
