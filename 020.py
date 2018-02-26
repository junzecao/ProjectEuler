# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python

import sys
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print sum(int(i) for i in str(factorial(n)))
