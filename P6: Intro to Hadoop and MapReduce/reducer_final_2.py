#!/usr/bin/python

import sys
import operator

oldid = None
count = 0
count1 = 0.0
y = 0.0

for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	
	if len(data_mapped)!= 3:
		continue

	newid, node_type, body = data_mapped
	
	if oldid and oldid!=newid:
		if y!=0:
			print oldid, "\t", count, "\t", count1, "\t", y
		else:
			print oldid, "\t", count, "\t", 0		
		oldid = newid
		count = 0
		count1 = 0
		y = 0		
	
	oldid = newid
	if node_type == "question":
		count += len(body)
	elif node_type == "answer":
		count1 += len(body)
		y +=1

if oldid !=None:
	if y!=0:
		print oldid, "\t", count, "\t", float(count1)/float(y)
	else:
		print oldid, "\t", count, "\t", 0		
