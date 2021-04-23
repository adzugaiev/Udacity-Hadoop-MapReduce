#!/usr/bin/python

# Loop around the data in the format key\tval
# For each key, print key, \t, mean(val)

import sys

sumVal = 0.0
cntVal = 0.0
oldKey = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2: # no pair, skip line
        continue
    
    key =   str(data[0])
    val = float(data[1])
    
    if oldKey != None and oldKey != key:
        print '{0}\t{1}'.format(oldKey, sumVal / cntVal)
        oldKey = key
        sumVal = 0.0
        cntVal = 0.0
    
    oldKey  = key
    sumVal += val
    cntVal += 1.0
    
if oldKey != None:
    print '{0}\t{1}'.format(oldKey, sumVal / cntVal)

