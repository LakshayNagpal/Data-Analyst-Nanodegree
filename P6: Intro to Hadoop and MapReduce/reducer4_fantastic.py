#!/usr/bin/python

import sys
import operator

sum = 0

for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	
	if len(data_mapped)!= 2:
		continue

	id, word = data_mapped
	
	print id
