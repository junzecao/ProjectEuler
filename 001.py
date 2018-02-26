#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    multiple = (n-1)/15
    remainder = n - multiple*15
    s = 60*(multiple) + 105*multiple*(multiple-1)/2
    if remainder is 0 or remainder is 1:
        print s
        continue
    partial = (remainder-1)/3
    s += partial*(partial+1)/2*3 + multiple*15*partial
    partial = (remainder-1)/5
    s += partial*(partial+1)/2*5 + multiple*15*partial
    print s
