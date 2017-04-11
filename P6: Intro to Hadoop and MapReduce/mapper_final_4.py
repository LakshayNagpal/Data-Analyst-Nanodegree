#!/usr/bin/python

import sys
import csv
import string

def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')
	for line in reader:
		id = line[0]
		author_id = line[3]
		print "{0}\t{1}".format(id,author_id)

def main():
	try:
		mapper()
	except:
		pass

main()

