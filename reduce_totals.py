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
    
    thisKey, thisVal = data
    
    if oldKey != None and oldKey != thisKey:
        oldKey = thisKey
    
    oldKey = thisKey
    sumVal += float(thisVal)
    cntVal += 1

if oldKey != None:
    print 'Sum', '\t', 'Count'
    print sumVal, '\t', cntVal

