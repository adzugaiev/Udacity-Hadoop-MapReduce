#!/usr/bin/python

# Map forum node author to node added hour.

import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
writer = csv.writer(sys.stdout, delimiter = '\t')

next(reader, None)          #skip csv header

for line in reader:
    if len(line) < 8:       # skip line with no added_at
        continue

    author_id = line[3].strip()
    added_at  = line[8].strip()
    
    if len(added_at) < 12:  # skip line with no hour
        continue

    hour = added_at[11:13]
    
    writer.writerow([author_id, hour])
