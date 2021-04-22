#!/usr/bin/python

# Loop around the data in the format key\tvalue
# For each key, print key, \t, all values comma & space separated

import sys

sumVal = ''
oldKey = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2: # no pair, skip line
        continue

    key = str(data[0])
    val = str(data[1])

    if oldKey != None and oldKey != key:
        print '{0}\t{1}'.format(oldKey, sumVal)
        oldKey = key
        sumVal = ''

    oldKey = key
    if len(sumVal) > 0: # needs comma separation
        sumVal += ', '
    sumVal += val

if oldKey != None:
    print '{0}\t{1}'.format(oldKey, sumVal)

