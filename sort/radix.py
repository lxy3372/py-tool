#!/usr/bin/env python
# -*- coding=utf-8 -*-

import math

__author__ = 'Riky'


def radix_sort(lists, radix):
    """

    :param lists: 待排序数组
    :param radix: 基数
    :return:
    """

    max_lenth = int(math.ceil(math.log(max(lists), radix)))  # 获取最大位数
    bucket = [[] for i in range(radix)]  # 初始化空桶
    for i in range(1, max_lenth + 1):  # 分别对每个位上的数进行排序 从个位到max_length 位
        for j in lists:
            key = j % (radix ** i) / (radix ** (i - 1))  # 获取当前J数,i位的值,即桶号
            bucket[key].append(j)
        del lists[:]
        for num_list in bucket:  # 排序完成回炉
            lists += num_list
            del num_list[:]

    return lists


if __name__ == "__main__":
    lists = [123, 4234, 12, 45, 7, 34, 3454, 238, 359, 76, 865]
    print radix_sort(lists, 10)
