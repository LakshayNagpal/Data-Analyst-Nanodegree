#!/usr/bin/python

import sys

count = 0
count1 = 0
oldKey = None
finalKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey!= thisKey:
	#print oldKey, "\t" , count
	if count1 < count:
	   count1 = count
	   finalKey = oldKey	
	
	oldKey = thisKey	
	count = 0

    oldKey = thisKey
    count +=1
if oldKey!= None:
	print finalKey , "\t" , count1

