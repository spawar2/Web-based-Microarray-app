#!/usr/bin/env python
'''
Author: Shrikant Pawar; Advanced Bio informatics; 2/18/2016
Description of this program: This program finds the sequences with 5, 6, 7, 8
histidine residue histags in input file and outputs the number of sequences.
'''
import re
query = open("pdbaanr.fasta", "r")

count = 0
for line in query:
    if re.search("HHHHH", line):
        print "Sequences with 5, 6, 7 and 8 histidine amino acid histag"
        count += 1
        print line
print "Number of sequences with histidine amino acid histag are: "
print count
        
        

