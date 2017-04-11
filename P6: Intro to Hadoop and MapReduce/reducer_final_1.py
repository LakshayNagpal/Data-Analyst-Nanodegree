#!/usr/bin/python

import sys
import operator

oldauthorid = None
hour = []
oldhour = 0

for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	
	if len(data_mapped)!= 2:
		continue

	newauthorid, newhour = data_mapped
	
	try:
		newhour = int(newhour)
	except ValueError:
		continue
	
	if oldauthorid and oldauthorid!=newauthorid:
		arr = [0]*24
		for i in hour:
			arr[i] +=1
		arr1 = []
		for i,x in enumerate(arr):
			if x == max(arr):
				arr1.append(i)

		print oldauthorid, "\t", arr1
		oldauthorid = newauthorid
		hour = []		
	
	oldauthorid = newauthorid
	hour.append(newhour)
	#oldhour = max(oldhour,newhour)

if oldauthorid !=None:
	print oldauthorid, "\t", oldhour
