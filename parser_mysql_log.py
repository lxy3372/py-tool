#!/usr/bin/env python
# -*- coding=utf-8 -*-f

"""
Valid logs format:
# Time: 150721 20:55:38
# User@Host: root[root] @  [10.169.93.18]
# Query_time: 10.101854  Lock_time: 0.000171 Rows_sent: 1  Rows_examined: 12988290
SET timestamp=1437483338;
SELECT * FROM test.t_test_user;
"""

from email.mime.text import MIMEText
import smtplib
import time
import os

__author__ = 'Riky'


def get_count(counter_file):
    """
    get lines counter
    """
    try:
        with open(counter_file) as file:
            count = int(file.readline())
    except:
        count = 0
        set_count(counter_file, str(count))
    return count


def set_count(counter_file, count):
    """
    set lines counter
    """
    with open(counter_file, 'w') as file:
        file.write(count)


def parser_log(log_file, start_line):
    """parse mysql-slow.log
    :param str log_file:日志文件地址
    :param str start_line:计数器文件地址
    :returns int lines_total, sql_list
    """
    p = os.popen("wc -l " + log_file + " | awk '{print $1}' ")  # only unix
    lines_total = p.read()
    with open(log_file) as log:
        i = 0
        sql_list = []
        data = {}
        for line in log.readlines()[start_line:len(log.readlines()) - 1]:
            if i is 0:
                data = {'sql': '', 'query_time': 0, 'date': 0}
            ret = line.find("# Time")
            if ret == 0:
                i = 1
                continue
            if i is 1:
                if line.find('# Query_time') == 0:
                    ext_list = line.strip('#').strip().split(" ")
                    data['query_time'] = ext_list[1]
                elif line.find('SET timestamp=') == 0:
                    data['date'] = int(line[14:].strip().strip(';'))
                    i = 2
                else:
                    pass
                continue

            if i is 2:
                data['sql'] += line.strip()
                if line.rfind(';') > 0:
                    i = 0
                    sql_list.append(data)
                    if len(sql_list) >= 100:
                        break
                    continue
    return lines_total, sql_list


def send_mail(sqls):
    sender = 'account@my.org'
    receiver = ['riky@my.org']
    subject = 'Mysql 慢查询日志'
    smtpserver = 'smtp.my.com'
    username = 'account@my.org'
    password = '****'
    content = "<br><br>" + subject + time.strftime("%Y-%m-%d") + "<br><br>" \
              "<div style='width:100%;'><table cellpadding='0' cellspacing='0' width='100%' style='border:1px solid #000;'><tr>" \
              "<th style='border:1px solid #ccc;text-align:center;'>SQL</th>" \
              "<th style='border:1px solid #ccc;text-align:center;'>耗时</th>"\
              "<th style='border:1px solid #ccc;text-align:center;'>查询时刻</th></tr>"
    if len(sqls) > 0:
        for data in sqls:
            content += "<tr>"
            content += "<td style='border:1px solid #ccc;text-align:center;'>" + data['sql'] + "</td>"
            content += "<td style='border:1px solid #ccc;text-align:center;'>" + data['query_time'] + "</td>"
            content += "<td style='border:1px solid #ccc;text-align:center;'>" + time.strftime("%Y-%m-%d %H:%I:%S", time.gmtime(data['date'])) + "</td>"
            content += "</tr>"
        content += "<tr><td colspan='3' style='text-align:center'>登陆服务器查看更多</td></tr>"
    else:
        content += "<tr><td colspan='3' style='text-align:center'>没有数据</td></tr>"
    content += "</table></div>"

    msg = MIMEText(content, 'html', 'utf-8')  # 中文需参数‘utf-8'，单字节字符不需要
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ";".join(receiver)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    try:
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
    except smtplib.SMTPAuthenticationError as e:
        print unicode(e.smtp_error, 'cp936')  # gbk to utf-8
    else:
        smtp.quit()


def run(log_file, counter_file):
    """
    :param str log_file:日志文件地址
    :param str counter_file:计数器文件地址
    """
    count = get_count(counter_file)
    lines_total, sql_list = parser_log(log_file, count)
    set_count(counter_file, str(lines_total))
    send_mail(sql_list)


if __name__ == "__main__":
    file = "./mysql-slow.log"
    counter_file = "./counter.txt"
    run(file, counter_file)
