#!/usr/bin/en python
# -*- coding:utf-8 -*-
"""
This file only runs on Windows
"""

import os
import time
import thread

__author__ = 'Riky'


def time_dir(other=''):
    """auto build for windows"""

    localtime = time.localtime(time.time())

    year = time.strftime('%Y', localtime);

    moon = time.strftime('%m', localtime);

    day = time.strftime('%d', localtime);

    varday = "\\" + year + "\\" + moon + "\\" + day

    cmd = r"explorer.exe \\192.168.60.209\192.168.60.187" + varday

    if other:
        cmd += "\\" + str(other)

    return cmd


def timer(no, interval):
    cnt = 0
    while cnt < 10:
        print 'Thread:(%d) Time:%s\n' % (no, time.ctime())
    time.sleep(interval)
    cnt += 1
    thread.exit_thread();


def linux_to_date(timestr):
    """
    date format to timestamp
    """
    timestr = float(timestr[:10])
    datetime = time.localtime(timestr)
    print time.strftime('%Y-%m-%d %H:%M:%S', datetime)


def timer_start():
    thread.start_new_thread(timer, (1, 1))
    thread.start_new_thread(timer, (2, 2))


if __name__ == '__main__':

    # start while
    while True:
        vardir = raw_input('Please input from the following item:')
        # item dir
        if (vardir == "downfile"):
            cmd = r"explorer.exe \\192.168.60.209\192.168.60.187\downfile"
        elif vardir == "liuzj":
            cmd = r"explorer.exe z:\workfile\liuzj"
        elif vardir == "localjob":
            cmd = r"explorer.exe z:\job"
        elif vardir == "admincompanyNew":
            cmd = r"explorer.exe z:\workfile\liuzj\admincompanyNew"
        elif vardir == "adminNew":
            cmd = r"explorer.exe z:\workfile\liuzj\adminNew"
        elif vardir == "myNew":
            cmd = r"explorer.exe z:\workfile\liuzj\myNew"
        elif vardir == "exit":
            print "Bye"
            exit()
        elif vardir == "linuxtime":
            vartime = raw_input("请给出需要转换的Linux时间戳：");
            linux_to_date(vartime)
            exit()
        elif vardir == "shutdown":
            os.system(r"shutdown -a");
        else:
            cmd = time_dir(vardir)

        try:
            os.system(cmd)
            print "loading..."
            print cmd
        # 为何弹窗还在
        except Exception, e:
            print 'No such file or directory', e
            break
        else:
            pass
        finally:
            pass
    # end while

    exit()
