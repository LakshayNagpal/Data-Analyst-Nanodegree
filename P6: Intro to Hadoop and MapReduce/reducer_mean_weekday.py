#!/usr/bin/python

import sys

total = 0.
#length = 0
#average = 0.
oldday = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisday, thiscost = data_mapped

    if oldday and oldday != thisday:
	#average = total / length        
	print oldday, "\t", total
        oldday = thisday;
        total = 0.
	#length = 0
	#average = 0.

    oldday = thisday
    total += float(thiscost)
    #length +=1

if oldday != None:
    #average = total / length
    print oldday, "\t", total

