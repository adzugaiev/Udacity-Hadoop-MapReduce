#!/usr/bin/python

# This mapper prepares to join the forum question and answer nodes.

# The output for the question node: 
# forum_nodes.id
# '1' if forum_nodes.node_type == 'question'
# len (forum_nodes.body)
# separated by \t

# The output for the answer node:
# forum_nodes.abs_parent_id (== question.id)
# '2' if forum_nodes.node_type == 'answer'
# len (forum_nodes.body)
# separated by \t

# The mapper key for both types of nodes is the question id: either
# forum_nodes.id or forum_nodes.abs_parent_id. During the sort and
# shuffle phases lines will be grouped based on the question id so
# the reducer can join quesion length to the vaerage answer length. 

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

next(reader, None)              # skip csv header

for line in reader:
    
    if len(line) < 8:           # skip corrupt lines
        continue
    
    if line[5] == 'question':   # question node
        # id, 1, len(body)
        writer.writerow([line[0]] + [1] + [len(line[4])])
    elif line[5] == 'answer':   # answer node
        # abs_parent_id, 2, len(body)
        writer.writerow([line[7]] + [2] + [len(line[4])])
    else:                       # another type of node, skip
        continue
