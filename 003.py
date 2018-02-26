#!/bin/python

import sys


def smallestDivisor(n):
    for i in xrange(3,int(n**0.5)+1,2):
        if not n%i:
            return i
    return n

t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    while not n%2:
        n = n>>1
    while True:
        divisor = smallestDivisor(n)
        if divisor is n:
            break
        n = n/divisor
    print divisor
