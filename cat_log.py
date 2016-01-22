#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""
This module provide functions about cutting log files
"""
import time
import os
import shutil

__author__ = 'Riky'


def cat_by_daily(old_file, new_file, pid_file):
    """cat log files by day
        1.rename the log file to the desctination path
        2.kill the nginx pid -USR1 to touch new log file
    """
    if not os.path.exists(old_file):
        return False
    shutil.move(old_file, new_file)
    # need root
    kill_sign = "/bin/kill -USR1 `cat %s`" % pid_file
    ret = os.system(kill_sign)
    return ret


if __name__ == "__main__":
    pid_file = "/var/run/nginx.pid"
    log_path = "/usr/local/var/log/nginx/"
    old_log_file = "access.log"
    new_log_file = old_log_file + "_" + time.strftime('%Y%m%d') + ".log"
    print cat_by_daily(log_path + old_log_file, log_path + new_log_file, pid_file)
