#!/usr/bin/python3
"""mapper.py"""

import sys

for line in sys.stdin:
	# Remove leading and trailing whitespace
	line = line.strip()
	# Get the fields
	fields = line.split('\t')
	
	if len(fields) == 2:
	    	# Genre data
	    	output = fields[0] + '\t-\t' + fields[1] + '\t-' * 8
	if len(fields) == 10:
    		# Review data
		output = fields[0] + '\t' + fields[1] + '\t-\t' + '\t'.join(fields[2:])
	
	print(output)
