#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    if n is 1 or n is 2:
        print 0
        continue
    elif n is 3:
        print 2
        continue
    a = 1
    b = 2
    c = 3
    count = 1
    total = 2
    while c < n:
        if not count%3:
            total += c
        count += 1
        a = b
        temp = b+c
        b = c
        c = temp
    print total
