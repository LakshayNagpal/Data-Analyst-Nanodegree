#!/usr/bin/python

import sys
import csv
import string


#for line in sys.stdin:
#	data = line.strip().split("\t")
#	if len(data) == 19:
#		id,b,c,d,body,node_type,g,h,i,j,k,l,m,n,o,p,q,r,s = data
#		print "{0}\t{1}\t{2}".format(id,node_type,body)

def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')
	for line in reader:
		id = line[0]
		node_type = line[5]
		body = line[4]
		print "{0}\t{1}\t{2}".format(id,node_type,body)

def main():
	try:
		mapper()
	except:
		pass

main()

