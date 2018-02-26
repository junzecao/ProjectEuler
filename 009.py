#!/bin/python

import sys
import math


def rounding(n):
    if abs(round(n)-n) < 0.0001:
        return int(round(n))
    return 0

def Pythagorean_triple(n):
    if n%2 or n<12:
        return -1
    
    start = int(math.ceil(max(n/3+1,n*(math.sqrt(2)-1))))
    for c in xrange(start,n/2):
        a = rounding((float(n-c))/2 - 0.5*math.sqrt(c*c + 2*c*n - n*n))
        if a:
            return c*n*(n-2*c)/2
    
    return -1

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print Pythagorean_triple(n)
