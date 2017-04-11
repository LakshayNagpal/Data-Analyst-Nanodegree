#!/usr/bin/python

import sys
import csv
import string


for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 19:
		a,b,c,author_id,e,f,g,h,added_at,j,k,l,m,n,o,p,q,r,s = data
		hour = added_at.split(" ")[-1].split(":")[0]
		print "{0}\t{1}".format(author_id,hour)
