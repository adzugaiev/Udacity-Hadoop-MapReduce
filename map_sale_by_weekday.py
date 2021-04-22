#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 0 (date for weekday) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re
from datetime import datetime as dt

valid_date = re.compile(r'([12]\d{3}-(0?[1-9]|1[0-2])-(0?[1-9]|[12]\d|3[01]))')
valid_cost = re.compile(r'^\d*\.?\d*$')

for line in sys.stdin:

    data = line.strip().split('\t')
    if len(data) < 5: # skip line with no cost
        continue

    date = data[0]
    cost = data[4]

    if valid_date.match(date) and valid_cost.match(cost):
        print '{0}\t{1}'.format(dt.strptime(date, '%Y-%m-%d').weekday(), cost)

