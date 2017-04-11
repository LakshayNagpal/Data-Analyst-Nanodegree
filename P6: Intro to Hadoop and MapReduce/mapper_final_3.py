#!/usr/bin/python

import sys
import csv
import string

def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')
	for line in reader:
		tagnames = line[2]
		tg = tagnames.split(" ")
		for x in tg:
			print "{0}\t{1}".format(x,1)

def main():
	try:
		mapper()
	except:
		pass

main()

