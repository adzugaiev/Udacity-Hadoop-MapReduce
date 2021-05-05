#!/usr/bin/python

# Map users to forum thread they have posted in. Thread is a question
# node with all it's answers and comments. If a user posted to that
# thread several times, they should be mapped several times as well,
# to indicate intensity of communication.

# Output: 
# forum_nodes.id if forum_nodes.node_type == 'question'
# or, for another node type
# forum_nodes.abs_parent_id (== question.id)
# forum_nodes.author_id
# separated by \t

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

next(reader, None)              # skip csv header

for line in reader:
    
    if len(line) < 8:           # skip corrupt lines
        continue
    
    if line[5] == 'question':   # question node
        # id, author_id 
        writer.writerow([line[0], line[3]])
    else:                       # another type of node
        # abs_parent_id, author_id
        writer.writerow([line[7], line[3]])
