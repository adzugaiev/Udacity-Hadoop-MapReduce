#!/usr/bin/python

# Map tags in forum_nodes.tagnames to 1 for question nodes.

import re
import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
writer = csv.writer(sys.stdout, delimiter = '\t')

next(reader, None)          # skip csv header

for line in reader:
    # skip lines other than questions
    if len(line) < 6: # no node_type
        continue
    if line[5] != 'question':
        continue

    tagnames = line[2].lower().strip()

    # split tagnames to tags
    tags = re.sub('[^\w]', ' ', tagnames).split()
    tags = list(set(tags))  # narrow tags to distinct
    
    for tag in tags:
        writer.writerow([tag, 1])
