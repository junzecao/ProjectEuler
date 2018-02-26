#!/bin/python

import sys


history = [1]

def CommonFactor(big,small):
    for i in xrange(2,small+1):
        if not big%i and not small%i:
            return i
    return 1

def LeastMultiple(big,small):
    multiple = big*small
    divisor = CommonFactor(big,small)
    while divisor is not 1:
        big /= divisor
        small /= divisor
        multiple /= divisor
        divisor = CommonFactor(big,small)
    return multiple

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    if n<len(history):
        print history[n]
    else:
        for small in xrange(len(history),n+1):
            history.append(LeastMultiple(history[small-1],small))
        print history[n]
