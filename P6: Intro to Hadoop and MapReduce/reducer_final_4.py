#!/usr/bin/python

import sys
import operator

oldid = None
dic = {}
lis = []

for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	
	if len(data_mapped)!= 2:
		continue

	newid, author_id = data_mapped

	if oldid and oldid!=newid:
		dic[oldid] = lis
		print oldid, "\t", dic[oldid]		
		oldid = newid
		lis = []		
	
	oldid = newid
	lis.append(author_id)
	

if oldid !=None:
	dic[oldid] = lis
	print oldid, "\t", dic[oldid]		
