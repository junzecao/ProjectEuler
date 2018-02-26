#!/bin/python

import sys


def SquareDifference(n):
    sum_small = 1
    for i in xrange(2,n+1):
        sum_small += i*i
    sum_big = (n**4 + 2*n**3 + n*n)/4
    return sum_big - sum_small

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print SquareDifference(n)
