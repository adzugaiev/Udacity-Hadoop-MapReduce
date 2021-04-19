#!/usr/bin/python

# Map unique words in the body of a forum node to the node id.

import re
import sys
import csv
from bs4 import BeautifulSoup #install: https://stackoverflow.com/a/22938434

reader = csv.reader(sys.stdin, delimiter = '\t')
writer = csv.writer(sys.stdout, delimiter = '\t')

next(reader, None) #skip csv header

for line in reader:
    if len(line) < 5:                           # skip line with no body
        continue
    node = line[0].strip()
    body = ' '.join(line[4].splitlines())       # remove line breaks
    soup = BeautifulSoup(body, 'html.parser')
    body = soup.get_text().lower()              # remove HTML, convert lowercase
    words = re.sub('[^\w]', ' ',  body).split() # split body to words
    words = list(set(words))                    # narrow words to distinct
    
    for word in words:
        writer.writerow([word, node])
