#!/bin/python

import sys


def largest_product(n,k,num):
    num = [int(i) for i in str(num)]
    max_product = 0
    for i in xrange(n-k+1):
        product = num[i]
        for j in xrange(i+1,i+k):
            product *= num[j]
        if max_product < product:
            max_product = product
    return max_product
            

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = raw_input().strip()
    print largest_product(n,k,num)
