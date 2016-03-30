#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
need pymysql: pip install pymysql
"""

from email.mime.text import MIMEText
from email.header import Header
import smtplib
import time
import pymysql

__author__ = 'Riky'


def main():
    conn = pymysql.connect(user='root', passwd='pwd', host='localhost', db='information_schema', charset='utf8')
    cur = conn.cursor()
    # update database
    sql = "select table_name, table_rows from tables where TABLE_SCHEMA in('test') order by table_rows desc";
    cur.execute(sql)

    send_mail(cur)

    conn.commit()
    cur.close()
    conn.close()


def send_mail(list):
    """
    :param list: tuple / list  (('table','total:int'), ('test', 1111))
    """
    sender = 'account@my.org'
    sender_nickname = 'Riky'
    receiver = ['riky@my.org']
    subject = 'Mysql 慢查询日志'
    smtpserver = 'smtp.my.com'
    username = 'account@my.org'
    password = '****'

    send_info = Header(sender_nickname, 'utf-8')
    send_info.append("<" + sender + ">", 'ascii')
    content = "<br><br>" + subject + time.strftime("%Y-%m-%d") + "<br><br>" \
                                                                 "<div style='width:100%;'><table cellpadding='0' cellspacing='0' width='100%' style='border:1px solid #000;'><tr>" \
                                                                 "<th style='border:1px solid #ccc;text-align:center;'>表名</th>" \
                                                                 "<th style='border:1px solid #ccc;text-align:center;'>当前数据条目</th></tr>"
    if list is not None:
        for data in list:
            total = data[1]
            color = 'red' if total > 300000 else ('yellow' if total > 200000 else '')
            content += "<tr style='background-color:" + color + ";'>"
            content += "<td style='border:1px solid #ccc;text-align:left;'>" + str(data[0]) + "</td>"
            content += "<td style='border:1px solid #ccc;text-align:left;'>" + str(data[1]) + "</td>"
            content += "</tr>"
        content += "<tr><td colspan='2' style='text-align:center'>登陆服务器查看更多</td></tr>"
    else:
        content += "<tr><td colspan='2' style='text-align:center'>没有数据</td></tr>"
    content += "</table></div>"

    msg = MIMEText(content, 'html', 'utf-8')  # 中文需参数‘utf-8'，单字节字符不需要
    msg['Subject'] = subject
    msg['From'] = send_info
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


if __name__ == '__main__':
    main()
