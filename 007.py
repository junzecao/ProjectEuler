#!/bin/python

import sys
import math


prime = [2,3]

def is_prime(n):
    sqrt_ = math.sqrt(n)
    for i in prime:
        if not n%i:
            return False
        if i>sqrt_:
            return True
    #return True

def add(index):
    len_ = len(prime)
    if len_ >= index:
        return
    n = prime[len_-1]
    while len_ < index:
        n += 2
        if is_prime(n):
            prime.append(n)
            len_ += 1
        
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    add(n)
    print prime[n-1]
