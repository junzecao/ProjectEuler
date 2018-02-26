#!/bin/python

import sys


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def all_palindrome():
    palindrome = []
    for i in xrange(100,1000):
        for j in xrange(i,1000):
            if i*j > 999999 or i*j < 100000:
                continue
            if is_palindrome(i*j):
                palindrome.append(i*j)
    palindrome = list(set(palindrome))
    palindrome.sort()
    return palindrome

palindrome = all_palindrome()
palindrome.append(1000000)
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    for i in xrange(len(palindrome)):
        if palindrome[i] >= n:
            print palindrome[i-1]
            break
