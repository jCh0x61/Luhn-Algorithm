#!/usr/bin/env python

# Luhn Algorithm - by xsp!d3r

import sys
import string
import re
import os

def Luhn_Algorithm(number):
	y=re.sub("\D", "", number)
	c = len(y) - 1
	parity = len(y) & 1
	sum=0

	while True:
		n=int(y[c])
		if c & 1 == parity:
			n*=2
		if n > 9:
			n = n - 9
		sum=sum+n
		c += -1
		if c < 0:
			break
	return ((sum % 10) == 0)
	


if len(sys.argv) < 2:
	print "Usage : " + os.path.basename(sys.argv[0]) + " input"
	exit()
	
input=sys.argv[1]
test = re.match('[0-9-\s]+$', input, re.IGNORECASE)
if test:
	result=Luhn_Algorithm(input)
	if result:
		print 'This number is valid'
	else:
		print 'This number is not valid'
else:
   print "Only numbers are allowed!"
