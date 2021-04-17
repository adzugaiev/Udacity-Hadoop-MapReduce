#!/usr/bin/python

# Loop around the data in the format key\tval
# Reduce to sum(val) and count(val)

import sys

sumVal = 0.0
cntVal = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2: # skip the corrupt line
        continue
    
    key, val = data
    
    if oldKey != None and oldKey != key:
        oldKey = key
    
    oldKey = key
    sumVal += float(val)
    cntVal += 1

if oldKey != None:
    print 'Sum', '\t', 'Count'
    print sumVal, '\t', cntVal

