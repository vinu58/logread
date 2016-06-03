#!/usr/bin/python
#read log files


print "Welcome to my log checking script"
print "#################################"

file=raw_input ('please enter the filename along with path (eg: /var/log/syslog)\n')
keyword=raw_input ('please enter the keyword to be searched(bluetooth or sigterm)\n')

with open( file, 'r' ) as f:
	for line in f:
		if keyword in line:
			print line


  

