# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 09:37:48 2014

@author: lifeix
"""

import re
import urllib2
import cookielib

url = 'http://www.php.net/manual/en/book.yaf.php'
#url = 'http://www.cnblogs.com/smileEvday/category/578973.html?page='
reg = '<a id="\w+" href="http://www.cnblogs.com/\w+/p/\w+.html">\s*\t*\n*\s*\t*\s*.*?\t*\n*\t*\s*</a>'

def startParse(author,page=1):
    
    cj = cookielib.LWPCookieJar()  
    cookie_support = urllib2.HTTPCookieProcessor(cj)  
    opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)  
    urllib2.install_opener(opener)  
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',  
           'Referer' : "http://www.cnblogs.com"}
           
    flag = True
    while flag == True:
        nurl = url + str(page)
        req = urllib2.Request(nurl,headers=headers)  
        resp = urllib2.urlopen(req)
        data = resp.read()
        regex = re.compile(reg,flags=re.MULTILINE)
        result = regex.findall(data)
        for d in result:
            print d
        if len(result) < 20:
            flag = False
        else:
            page = page + 1
    print 'finished----------------------page:%d'%page
    
    
if __name__ == '__main__':
    startParse('',1)
