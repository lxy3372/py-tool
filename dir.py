#-*- conding:gbk -*-
#coding=gbk

import os
import time
import thread


##
# @brief time_dir 
#
# @param other
#
# @return 
def time_dir(other=''):
	"""这可真的是无语了"""

	localtime = time.localtime(time.time())
	
	year = time.strftime('%Y',localtime);
	
	moon = time.strftime('%m',localtime);
	
	day = time.strftime('%d',localtime);
	
	varday = "\\"+year+"\\"+moon+"\\"+day
	
	cmd = r"explorer.exe \\192.168.60.209\192.168.60.187"+varday

	if other:
		cmd += "\\"+str(other)

	return cmd

def timer(no,interval):
	cnt = 0
	while cnt<10:
		print 'Thread:(%d) Time:%s\n'%(no, time.ctime())  
        time.sleep(interval)  
        cnt+=1 
	thread.exit_thread();
		
def linux_to_date(timestr):

	timestr = float(timestr[:10])
	datetime = time.localtime(timestr)
	print time.strftime('%Y-%m-%d %H:%M:%S',datetime)


##
# @brief timer_start 
# 启动线程
# @return 
def timer_start():
	thread.start_new_thread(timer,(1,1))
	thread.start_new_thread(timer,(2,2))

if __name__=='__main__':

	#start while
	while True:
		vardir = raw_input('请给执行命令:')
		#下载目录
		if(vardir=="downfile"):
			cmd = r"explorer.exe \\192.168.60.209\192.168.60.187\downfile"
		elif vardir == "common" :
			cmd = r"explorer.exe z:\job\incjob1001variable\dbBase\modelsCommon\modelsCommon"
		elif vardir == "liuzj" :
			cmd = r"explorer.exe z:\workfile\liuzj"
		elif vardir == "localjob" :
			cmd = r"explorer.exe z:\job"
		elif vardir == "admincompanyNew":
			cmd = r"explorer.exe z:\workfile\liuzj\admincompanyNew"
		elif vardir == "adminNew":
			cmd = r"explorer.exe z:\workfile\liuzj\adminNew"
		elif vardir == "myNew":
			cmd = r"explorer.exe z:\workfile\liuzj\myNew"
		elif vardir == "210" :
			cmd = r"explorer.exe \\192.168.60.210\program_upload\l刘志坚"
		elif vardir == "exit":
			print "Bye"
			exit()
		elif vardir == "linuxtime":
			vartime = raw_input("请给出需要转换的linux时间戳：");
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
		#为何弹窗还在
		except Exception,e:
			print '没有找到目录',e
			break
		else:
			pass
		finally:
			pass
	#end while

	exit()
