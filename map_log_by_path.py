#!/usr/bin/python

# Format of each line is anonymized Common Log Format:
# https://stackoverflow.com/a/12544587
#
# We want to count hits per path
# We need to write path and hit (1) to standard output, separated by a tab

import sys
import re
import urlparse as url

expr = re.compile(r'([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (.+)')

for line in sys.stdin:
    
    log = re.match(expr, line)
    if not log: # skip line if not parsed
        continue
    
    request = log.group(3).strip().split(' ')
    if len(request) < 2: #request has no page
        continue
    
    print url.urlparse(request[1]).path, '\t', 1

