#!/usr/bin/python

# Loop around the data in the format key\tval
# Reduce val to max(val) per key

import sys

maxVal = 0.0
oldKey = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2: # skip the corrupt line
        continue

    key, val = data

    if oldKey != None and oldKey != key:
        print oldKey, '\t', maxVal
        oldKey = key
        maxVal = 0.0

    oldKey = key
    if float(val) > maxVal:
        maxVal = val

if oldKey != None:
    print oldKey, '\t', maxVal

