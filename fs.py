#-*- coding:gbk-*-  
#coding=gbk
  
# 检索目录下所有文件中包含指定字符串的文件  
import os  
import re  
  
# 枚举dirPath目录下的所有文件  
def listFiles(dirPath):  
#begin  
    fileList = []  
    for root, dirs, files in os.walk(dirPath):          # 注意os.walk的功能  
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
			print str(j)+"文件："+str(filePath)+"	第"+str(i)+"行:"
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
		fileDir = raw_input("请输入文件目录：");
		if fileDir == 'exit':
			print "Bye"
			exit()
		elif os.path.exists(fileDir) is False:
			print "文件目录不存在"
			fileDir = False
		else:
			os.system('cls')
	while regex == '' or regex == False:
		regex = raw_input("请输入要查找的字符：");
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
	print "共找到"+str(findCount)+"个文件中含有"+str(regex)
	os.system("pause")
#end  
  

if __name__ == '__main__':
#begin  
    main()
#end  

