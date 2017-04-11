#!/usr/bin/python

import sys
import re

for line in sys.stdin:
	#regex = '([(\d.)]+) - - [(.?)] "(.?)" (\d+) (.*)'
	#data = line.strip()
	#data = re.match(regex,line)
	#new_data = line.split('"GET "')[].split('" HTTP/1.1"')[0]
	data = line.split()
	data = data[6]
	url = "http://www.the-associates.co.uk"
	if url in data:
		data = data[len(url):]
	
	print "{0}\t{1}".format(data, 1)
	#if len(data) == 5:
	    #ip, time, request, status, byte = data
	    #print "{0}\t{1}".format(request,status)
