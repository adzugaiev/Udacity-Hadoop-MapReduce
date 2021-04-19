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

    key, val = data

    if oldKey and oldKey != key:
        print oldKey, '\t', sumVal
        oldKey = key
        sumVal = ''

    oldKey = key
    if len(sumVal) > 0: # needs comma separation
        sumVal += ', '
    sumVal += str(val)

if oldKey != None:
    print oldKey, '\t', sumVal

