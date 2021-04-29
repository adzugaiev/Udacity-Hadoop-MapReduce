#!/usr/bin/python

# Loop around the data in the format key\tval
# Reduce val to most frequent val(s) per key

import sys

valCnt = {} # value counts per key
oldKey = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2: # skip the corrupt line
        continue
    
    key = str(data[0])
    val = str(data[1])
    
    if oldKey != None and oldKey != key:
        maxCnt = max(valCnt.values())
        for value, count in valCnt.items():
            if count == maxCnt:
                print '{0}\t{1}'.format(oldKey, value)
        oldKey = key
        valCnt = {}
    
    oldKey = key
    if val in valCnt:
        valCnt[val] += 1
    else: valCnt[val] = 1
    
if oldKey != None:
    maxCnt = max(valCnt.values())
    for value, count in valCnt.items():
        if count == maxCnt:
            print '{0}\t{1}'.format(oldKey, value)

