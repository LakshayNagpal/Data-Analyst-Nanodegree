#!/usr/bin/python

import sys
import operator

oldtag = None
count1 = 0
dic = {}
sorted_dict = {}

for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	
	if len(data_mapped)!= 2:
		continue

	newtag, count = data_mapped
	
	try:
		count = int(count)
    	except ValueError :
		continue

	if oldtag and oldtag!=newtag:
		dic[oldtag] = count1		
		oldtag = newtag
		count1 = 0		
	
	oldtag = newtag
	count1 += count

if oldtag !=None:
	dic[oldtag] = count1

sorted_dict = sorted(dic.items(),key=operator.itemgetter(1), reverse=True)

for i in range(10):
	print sorted_dict[i]		
