#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""only windows"""
import os
import re


def listFiles(dirPath):
    fileList = []
    for root, dirs, files in os.walk(dirPath):
        for fileObj in files:
            fileList.append(os.path.join(root, fileObj))
    return fileList


def findString(filePath, regex, j):
    isFind = False
    fileObj = open(filePath, 'r')
    for i, eachLine in enumerate(fileObj):
        if re.search(regex, eachLine, re.I):
            print str(j) + "�ļ���" + str(filePath) + "	��" + str(i) + "��:"
            print str(eachLine) + "\n\n"
            isFind = True
            break
    return isFind


def main():
    fileDir = False
    regex = False
    while fileDir == '' or fileDir == False:
        fileDir = raw_input("�������ļ�Ŀ¼��");
        if fileDir == 'exit':
            print "Bye"
            exit()
        elif os.path.exists(fileDir) is False:
            print "�ļ�Ŀ¼������"
            fileDir = False
        else:
            os.system('cls')
    while regex == '' or regex == False:
        regex = raw_input("������Ҫ���ҵ��ַ���");
    else:
        os.system('cls')

    print 'loading...'
    fileList = listFiles(fileDir)
    print "load " + str(len(fileList)) + " files\n"
    print 'searching...'
    findCount = 0
    for j, fileObj in enumerate(fileList):
        if (findString(fileObj, regex, j) is True):
            findCount += 1
    print "���ҵ�" + str(findCount) + "���ļ��к���" + str(regex)
    os.system("pause")


if __name__ == '__main__':
    main()
