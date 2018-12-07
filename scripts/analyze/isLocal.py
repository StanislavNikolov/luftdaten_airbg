#!/bin/env python3

import sys

filelist = sys.stdin.read().split('\n')

latB = 42.6161
latE = 42.7571
lonB = 23.2488
lonE = 23.4481

for fname in filelist:
	try:
		with open(fname) as f:
			record = f.readlines()[1:2][0].split(';')
			lat = float(record[3])
			lon = float(record[4])
			if latB <= lat and lat <= latE and lonB <= lon and lon <= lonE:
				print(fname)
	except:
		pass # TODO print to stderr
