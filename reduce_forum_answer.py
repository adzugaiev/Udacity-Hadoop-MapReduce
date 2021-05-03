#!/usr/bin/python

# Mapper: map_forum_answer.py
# Reducer joins by node id the tsv lines of two types:
# Line that starts with node id then 1 then question_length
# Line that starts with node id then 2 then answer_length
# Reduce to question_length \t mean(answer_length)

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

queLen = 0.0 # current question's length
sumAns = 0.0 # sum of answers' length to the current question
cntAns = 0.0 # count of answers to the current question

for line in reader:
    if len(line) != 3:          # skip corrupt line
        continue
    
    lineType = int(line[1])
    
    if lineType == 1:           # question line
        if queLen and cntAns:   # previous question has answers
            writer.writerow([queLen, sumAns / cntAns])
        queLen = float(line[2])
        sumAns = 0.0
        cntAns = 0.0
    elif lineType == 2:         # answer line
        sumAns += float(line[2])
        cntAns += 1.0
    else:                       # unknown line
        continue
    
if queLen and cntAns:           # last question has answers
    writer.writerow([queLen, sumAns / cntAns])
