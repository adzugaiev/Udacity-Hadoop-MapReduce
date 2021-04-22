#!/usr/bin/python

# Loop around the data in the format key\tval
# Reduce val to max(val) per key

import sys

maxVal = 0.0 # this assumes values are positive
oldKey = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2: # skip the corrupt line
        continue

    key =   str(data[0])
    val = float(data[1])

    if oldKey != None and oldKey != key:
        print '{0}\t{1}'.format(oldKey, maxVal)
        oldKey = key
        maxVal = 0.0

    oldKey = key
    if val > maxVal:
        maxVal = val

if oldKey != None:
    print '{0}\t{1}'.format(oldKey, maxVal)

