#!/usr/bin/python

# Loop around the data in the format key\tval
# Reduce to top N lines by float(val)

import sys

N = 5 # top N
ascending = False # top N ascending, otherwise descending
top_lines = [['Empty', 0.0] for i in range(N)]

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2: # skip the corrupt line
        continue
    
    key = data[0]
    val = float(data[1])
    
    # find current line's position in top N, if any
    top_i = -1
    for i in range(N):
        if val > top_lines[i][1]:
            top_i = i
    
    # if current line gets in top N, put it there
    if top_i >= 0:
        # move top lines below top_i down 1 position
        for i in range(top_i):
            top_lines[i][0] = top_lines[i+1][0]
            top_lines[i][1] = top_lines[i+1][1]
        # put current line in position top_i                
        top_lines[top_i][0] = key
        top_lines[top_i][1] = val

# after processing all lines, write final top N
for top_line in (top_lines if ascending else top_lines[::-1]):
    print top_line[0], '\t', top_line[1]
    
