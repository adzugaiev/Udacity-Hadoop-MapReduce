#!/usr/bin/python

# Format of each line is anonymized Common Log Format:
# https://stackoverflow.com/a/12544587
#
# We want to count hits per ip
# We need to write ip and hit (1) to standard output, separated by a tab

import sys
import re

expr = re.compile(r'([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (.+)')

for line in sys.stdin:

    log = re.match(expr, line)
    if not log: # skip line if not parsed
        continue
    
    ip = log.group(1).strip()
    if len(ip) < 1: #line has no ip
        continue

    print ip, '\t', 1

