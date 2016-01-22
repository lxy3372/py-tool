#!/usr/bin/en python
# -*- coding:utf-8 -*-

from json import *

__author__ = 'Ricky'


def analysis_log(file_path):
    """
    解析日志
    :param file_path:文件路径
    :type file_path:string
    :return:
    :rtype:
    """

    try:
        with open(file_path) as file:
            i = 1
            for line in file:
                result = get_line_dict(line)
                if (result is False):
                    print("error")
                else:
                    print(result)
                i = i + 1
            print("total %d lines" % i)
    except FileNotFoundError as e:
        print("can not found the files")
    finally:
        print('done.')


def get_line_dict(log_str):
    """
    获取每行推送关键信息
    :param log_str:每行日志
    :type log_str: string
    :return: dict
    :rtype:
    """

    push_time = log_str[:21].strip().lstrip('[').rstrip(']')
    pos = log_str.find("body")

    if log_str.find('retryTimes') > -1:
        new_log_str = log_str[pos + 7:-21]
    else:
        new_log_str = log_str[pos + 7:-6]

    new_log_str = new_log_str.replace('\\', '')
    try:
        re = JSONDecoder().decode(str(new_log_str))
    except Exception:
        return False

    notices_list = dict()

    if (re['platform'] == 'all'):
        content = re['message']
        notices_list['title'] = content['msg_content']
    elif (re['platform'] == ['ios']):
        notification = re['notification']
        content = notification['ios']
    else:
        return False

    notices_list = dict()
    notices_list['pushTime'] = push_time
    notices_list = dict(notices_list, **content['extras'])

    return notices_list


if __name__ == "__main__":
    file = "/Users/CHDXY/Workspace/Shell/jpush.log"
    analysis_log(file)
