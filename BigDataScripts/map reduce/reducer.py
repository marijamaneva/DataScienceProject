#!/usr/bin/python3
"""reducer.py"""

import sys

title = None
genre = None

for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# parse the input from mapper.py
	fields = line.split('\t')
    
	if fields[2] != '-':
		# Save the title and genre of a movie
		title = fields[0]
		genre = fields[2]
	else:
		if fields[0] == title:
			# There is a match in the genre dataset
			output = title + '\t' + fields[1] + '\t' + genre + '\t' + '\t'.join(fields[3:])
		else:
			# There is no information about genre
			output = fields[0] + '\t' + fields[1] + '\t' + '-' + '\t' + '\t'.join(fields[3:])
			
		print(output)
			
