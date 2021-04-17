#!/usr/bin/python

# Loop around the data in the format key\tval
# For each key, print key, \t, sum(val)

import sys

sumVal = 0.0
oldKey = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2: # no pair, skip line
        continue

    key, val = data

    if oldKey and oldKey != key:
        print oldKey, '\t', sumVal
        oldKey = key
        sumVal = 0.0

    oldKey = key
    sumVal += float(val)

if oldKey != None:
    print oldKey, '\t', sumVal

