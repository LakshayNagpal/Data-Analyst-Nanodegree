#!/usr/bin/python

import sys
import operator

for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	
	if len(data_mapped)!= 3:
		continue

	newid, node_type, body = data_mapped
	
	if node_type == "answer":
		print newid,"\t", node_type,"\t", body
