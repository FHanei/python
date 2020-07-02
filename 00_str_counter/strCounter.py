#.......................................#
#a script to count strings
#Author: Fei Han
#Date  : 6/30/2020
#Usage :
#      python strCounter.py logFile
#.......................................#

import sys
import os
import logging

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

#You can modify below two string
#This is start string for one cycle
startStr = "abl-APL"
#This is target string
targetStr = "dimensions H"

if len(sys.argv) == 2:
	logFile = sys.argv[1]
else:
	logging.error("Please input log file with full path")
	quit()

if not os.path.isfile(logFile):
	logging.error("log file not exist")
	quit()

logFileObj = open(logFile, 'r')
if not logFileObj:
	logging.error("can't open log file")
	quit()

outFileObj = open('./result.log', 'w');
if not outFileObj:
	logging.error("can't open out file")
	quit()

times = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def find_str(targetStr):
	ret = 0
	oneLineLog = logFileObj.readline();
	while oneLineLog:
		if oneLineLog.count(targetStr):
			ret = 1
			break
		else:
			oneLineLog = logFileObj.readline();
			continue
	
	logging.debug(oneLineLog)

	return ret

def count_str(targetStr):
	#find target first
	if not find_str(targetStr):
		logging.debug("can't find %s in %s", startStr, logFile)
		return -1

	#count it
	ret = 1
	oneLineLog = logFileObj.readline();
	while oneLineLog:
		if oneLineLog.count(targetStr):
			ret = ret + 1
			oneLineLog = logFileObj.readline();
		elif oneLineLog.count(startStr):
			logFileObj.seek(-1, os.SEEK_CUR);
			break
		else:
			oneLineLog = logFileObj.readline();
			continue
	
	return ret

while 1:
	#find start string first
	if not find_str(startStr):
		logging.debug("can't find %s in %s" % (startStr, logFile))
		break

	#find target and count it
	ret = count_str(targetStr)
	if ret > 0:
		logging.debug("%d", ret)
		times[ret] = times[ret] + 1
	elif ret < 0:
		break


for x in range(1, len(times), 1):
	logging.info("%dth read success occurs times: %d", x, times[x])
	outFileObj.write('%ith read sum times: %i\n' % (x, times[x]))

logFileObj.close()
outFileObj.close()

logging.info("DONE")