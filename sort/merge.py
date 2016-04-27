#!/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'Riky'


def my_merge(lists):
    if len(lists) <= 1:
        return lists
    mid = int(round(len(lists) / 2, 0))
    left= lists[0:mid]
    right= lists[mid:]
    left_list = my_merge(left)
    right_list = my_merge(right)
    left_len = len(left_list)
    right_len = len(right_list)
    i = 0
    j = 0
    new_list = []
    while i < left_len and j < right_len:
        if left_list[i] < right_list[j]:
            new_list.append(left_list[i])
            i += 1
        else:
            new_list.append(right_list[j])
            j += 1
    if i < left_len:
        new_list.append(left_list[i])

    if j < right_len:
        new_list.append(right_list[j])

    return new_list


if __name__ == "__main__":
    lists = [32, 12, 57, 21, 36, 95, 34, 87, 13]
    print my_merge(lists)
