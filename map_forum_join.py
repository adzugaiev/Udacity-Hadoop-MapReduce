#!/usr/bin/python

# This mapper prepares to join the forum node and forum user data:
# forum_nodes.tsv and forum_users.tsv

# The output from the reducer for each forum post should be: 
# forum_nodes.id
# forum_nodes.title
# forum_nodes.author_id
# forum_nodes.node_type
# forum_nodes.added_at
# forum_nodes.score
# forum_users.reputation
# separated by \t

# The mapper should take in records from both forum_node and forum_users
# and keep, for each record, those fields that are needed for the reducer
# output. The mapper will start each line with user id followed by the
# line type (1 = user, 2 = node) to mark where it comes from (user data
# or node data).

# The mapper key for both types of lines is the user id: either
# forum_users.user_ptr_id or forum_nodes.author_id. During the sort and
# shuffle phases lines will be grouped based on the user id so the
# reducer can process and join them appropriately. 

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

next(reader, None) # skip csv header

for line in reader:
    
    if len(line) < 5:   # skip corrupt lines
        continue
    
    if len(line) ==  5:
        # user line, should come before user's node lines
        # user_ptr_id, 1, reputation
        writer.writerow([line[0]] + [1] + [line[1]])        
    else:
        # node line, should follow user's line
        # author_id, 2, id, title, author_id, node_type, added_at, score
        writer.writerow([line[3]] + [2] + line[:2] + [line[3]] + [line[5]] + line[8:10])      
