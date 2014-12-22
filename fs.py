#-*- coding:gbk-*-  
#coding=gbk
  
# ����Ŀ¼�������ļ��а���ָ���ַ������ļ�  
import os  
import re  
  
# ö��dirPathĿ¼�µ������ļ�  
def listFiles(dirPath):  
#begin  
    fileList = []  
    for root, dirs, files in os.walk(dirPath):          # ע��os.walk�Ĺ���  
    #begin  
        for fileObj in files:  
        #begin  
            fileList.append(os.path.join(root, fileObj))  
        #end  
    #end  
    return fileList  
#end  
  
def findString(filePath, regex,j):  
#begin  
	isFind = False
	fileObj = open(filePath, 'r')
	for i,eachLine in enumerate(fileObj):  
    #begin  
		if re.search(regex, eachLine, re.I):  
        #begin
			print str(j)+"�ļ���"+str(filePath)+"	��"+str(i)+"��:"
			print str(eachLine)+"\n\n"
			isFind = True
			break
        #end
    #end
	return isFind
#end
  
  
def main():  
#begin  
	fileDir = False
	regex = False
	while fileDir=='' or fileDir == False:
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
	print "load "+str(len(fileList))+" files\n"
	print 'searching...'
	findCount = 0
	for j,fileObj in enumerate(fileList):
    #begin
		if(findString(fileObj,regex,j) is True):
			findCount += 1
    #end
	print "���ҵ�"+str(findCount)+"���ļ��к���"+str(regex)
	os.system("pause")
#end  
  

if __name__ == '__main__':
#begin  
    main()
#end  

