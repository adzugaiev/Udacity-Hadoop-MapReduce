#!/usr/bin/python

# Mapper: map_forum_join.py
# Reducer joins the tsv lines that come from 2 sources:
# Line that starts with userid then 1 is the user data
# Line that starts with userid then 2 is the forum node data

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

user = None # all data of current user
node = None # all data of current node
join = None # current node join current user

for line in reader:
    if len(line) < 3:   # skip corrupt line
        continue
    
    ltyp = int(line[1]) # line type
    if ltyp == 1:       # user line
        user = line
        node = None
    elif ltyp == 2:     # node line
        node = line
    else:               # skip unknown line
        continue
    
    if user and node: # at least 1 node present for user
        join = node[2:] + user[2:]
        writer.writerow(join)
