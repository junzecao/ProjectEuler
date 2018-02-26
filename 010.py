#!/bin/python

import sys
import math


bin_ = 2000

def is_prime(n):
    # even numbers (including 2) are taken care of elsewhere
    for i in xrange(3,int(math.sqrt(n))+1,2):
        if n%i == 0:
            return False
    return True

limit = [0] * bin_
bucket_size = 1000000/bin_
def make_limit():
    bucket_index = 0
    sum_ = 2
    for i in xrange(3,1000000,2):
        if is_prime(i):
            sum_ += i
        if i == ((bucket_index+1)*bucket_size-1):
            limit[bucket_index] = sum_
            bucket_index += 1

def summation(n):
    bucket = n/bucket_size
    if bucket == 0:
        if n == 1:
            return 0
        sum_ = 2
        for i in xrange(3,n+1,2):
            if is_prime(i):
                sum_ += i
        return sum_
    
    sum_ = limit[bucket-1]
    for i in xrange(bucket*bucket_size+1,n+1,2):
        if is_prime(i):
            sum_ += i
    return sum_

make_limit()
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print summation(n)
