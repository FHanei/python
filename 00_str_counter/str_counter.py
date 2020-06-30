#.......................................#
#a script to count strings
#Author: Fei Han
#Date  : 6/30/2020
#Usage :
#      python str_count.py input_file
#.......................................#

import sys
import os

#You can modify below two string
#This is start string for one cycle
boot_string = "abl-APL"
#This is target string
target_string = "dimensions H"

if len(sys.argv) == 2:
	log_file = sys.argv[1]
else:
	print "Please input log file with full path"
	quit()

if not os.path.exists(log_file):
	print "log file not exist"
	quit()

log_file_object = open(log_file, 'r')
if not log_file_object:
	print "can't open log file"

out_file_object = open('./outfile.log', 'w');
if not log_file_object:
	print "can't open out file"

times = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while 1:
	oneline_log = log_file_object.readline()
	if oneline_log.count(boot_string):
		counter = 0
	elif not oneline_log:
		break
	else:
		continue

	while not log_file_object.readline().count(target_string):
		continue

	counter = 1

	while log_file_object.readline().count(target_string) == 1:
		counter = counter + 1

	times[counter] = times[counter] + 1
	#print counter

for x in range(len(times)):
	print times[x]
	out_file_object.write('%ith read sum times: %i\n' % (x, times[x]))

log_file_object.close()
out_file_object.close()

print "DONE"
