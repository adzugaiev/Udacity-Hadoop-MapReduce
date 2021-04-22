#!/usr/bin/python

# Loop around the data in the format key\tval
# Reduce to sum(val) and count(val)

import sys

sumVal = 0.0
cntVal = 0

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2: # skip the corrupt line
        continue
    
    val = float(data[1])
    
    sumVal += val
    cntVal += 1

print 'Sum\tCount'
print '{0}\t{1}'.format(sumVal, cntVal)

