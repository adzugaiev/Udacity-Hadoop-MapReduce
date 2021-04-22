#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 3 (item) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re

valid_item = re.compile(r'^(.|\s)*\w(.|\s)*$')
valid_cost = re.compile(r'^\d*\.?\d*$')

for line in sys.stdin:

    data = line.strip().split('\t')
    if len(data) < 5: # skip line with no cost
        continue

    item = data[3]
    cost = data[4]

    if valid_item.match(item) and valid_cost.match(cost):
        print '{0}\t{1}'.format(item, cost)

